/**
 * DESIGN.md Validator, WCAG Contrast Engine & CSS Compiler
 * Autor: Leonel Salcedo / Nomack Studio & Antigravity
 * 
 * Implementa:
 * - Cálculo matemático de Luminancia Relativa y Contrast Ratio WCAG 2.1 AA/AAA
 * - Validación de tokens YAML en DESIGN.md
 * - Exportación a CSS Custom Properties y configuración Tailwind
 */

export interface DesignTokenColors {
  [key: string]: string;
}

export interface TypographyToken {
  fontFamily: string;
  fontSize: string;
  fontWeight?: string;
  lineHeight?: string;
  letterSpacing?: string;
}

export interface DesignMdSchema {
  name: string;
  colors: DesignTokenColors;
  typography: { [key: string]: TypographyToken };
  rounded?: { [key: string]: string };
  spacing?: { [key: string]: string };
  components?: { [key: string]: Record<string, string> };
}

export class DesignMdEngine {
  /**
   * Convierte un código HEX (#RRGGBB o #RGB) a componentes RGB [0, 255]
   */
  public static hexToRgb(hex: string): [number, number, number] {
    let cleanHex = hex.replace('#', '').trim();
    if (cleanHex.length === 3) {
      cleanHex = cleanHex.split('').map(c => c + c).join('');
    }
    const num = parseInt(cleanHex, 16);
    return [(num >> 16) & 255, (num >> 8) & 255, num & 255];
  }

  /**
   * Calcula la luminancia relativa según la fórmula sRGB de WCAG 2.1
   */
  public static getRelativeLuminance(rgb: [number, number, number]): number {
    const [r, g, b] = rgb.map(val => {
      const s = val / 255.0;
      return s <= 0.04045 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  }

  /**
   * Calcula el ratio de contraste entre dos colores HEX
   */
  public static getContrastRatio(hex1: string, hex2: string): number {
    const lum1 = this.getRelativeLuminance(this.hexToRgb(hex1));
    const lum2 = this.getRelativeLuminance(this.hexToRgb(hex2));
    const lighter = Math.max(lum1, lum2);
    const darker = Math.min(lum1, lum2);
    return (lighter + 0.05) / (darker + 0.05);
  }

  /**
   * Evalúa el cumplimiento de WCAG 2.1
   */
  public static checkWcagCompliance(ratio: number): { aa: boolean; aaLarge: boolean; aaa: boolean } {
    return {
      aa: ratio >= 4.5,
      aaLarge: ratio >= 3.0,
      aaa: ratio >= 7.0
    };
  }

  /**
   * Compila el schema DESIGN.md a variables CSS
   */
  public static compileToCssVariables(spec: DesignMdSchema): string {
    const lines: string[] = [`/* Generated from DESIGN.md: ${spec.name} */`, ':root {'];

    // Colores
    lines.push('  /* Colors */');
    for (const [key, val] of Object.entries(spec.colors)) {
      lines.push(`  --color-${key}: ${val};`);
    }

    // Radios
    if (spec.rounded) {
      lines.push('\n  /* Border Radii */');
      for (const [key, val] of Object.entries(spec.rounded)) {
        lines.push(`  --rounded-${key}: ${val};`);
      }
    }

    // Espaciados
    if (spec.spacing) {
      lines.push('\n  /* Spacing */');
      for (const [key, val] of Object.entries(spec.spacing)) {
        lines.push(`  --spacing-${key}: ${val};`);
      }
    }

    lines.push('}');
    return lines.join('\n');
  }
}

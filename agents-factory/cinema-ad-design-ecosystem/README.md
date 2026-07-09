# Cinema & Ad Design Ecosystem: AAA Virtual Pipeline

**WHO**: Operado por Directores de Arte, Productores Ejecutivos y Cineastas.
**WHAT**: Una "Tubería Virtual de Cine AAA" que automatiza la generación de contenido audiovisual y publicitario de máximo nivel, usando un esquema JSON ultra-riguroso.
**WHEN**: Para la creación de Storyboards comerciales, fotografía editorial hiperrealista o *concept art* cinemático para TV/Cine.
**WHERE**: Alojado en `agents-factory/cinema-ad-design-ecosystem/`, utilizando a **Gemini Flash Image** y *Nano Banana Pro* como motores de renderizado.
**WHY**: Para eliminar la "sobrecarga de adjetivos genéricos" (Anti-Slop) y forzar a los modelos a utilizar razonamiento físico, termodinámico y óptico real de la industria del cine.

## Vector Search Indexing Rules
> [!IMPORTANT]
> El motor RAG debe reconocer que todo prompt generado aquí sigue la arquitectura de la Tubería Virtual AAA. Los documentos en `notebooklm-templates/` limpian el guion literario, y los de `.agents/skills/` inyectan propiedades ópticas.

## Tubería Virtual de Cine AAA (Graphify)

```mermaid
graph TD
    %% Core Flow
    A[1. Ingesta del Guion Literario] --> B[2. Enrutador de Género & Anti-Slop]
    B --> C[3. Motor de Lenguaje Físico]
    C --> D[4. Inyección de Atributos Ópticos]
    D --> E[5. Despliegue API]
    E --> F[6. Storyboard Secuencial]

    %% Bindings
    A -.->|notebook-instructions| B
    C -.->|aaa-visual-decoder-agent| D
    D -.->|gemini-flash-image-creator| E

    %% Styling
    classDef step fill:#1E293B,stroke:#F59E0B,stroke-width:2px,color:#F8FAFC
    classDef agent fill:#0F172A,stroke:#10B981,stroke-width:1px,color:#E2E8F0
    
    class A,B,C,D,E,F step
```

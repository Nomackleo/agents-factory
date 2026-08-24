# Reglas de Ciberseguridad y Parametrización: Google Workspace Enterprise

**DOMINIO**: `agents-factory/google-workspace-ecosystem/`  
**ESTÁNDARES OBLIGATORIOS**: ISO/IEC 27001:2022, ISO 9001:2015, ISO/IEC 42001:2023, SOC 2 y NIST CSF.  

---

## 1. Reglas Inmutables de Identidad y Acceso (IAM)

1. **Obligatoriedad de 2FA/MFA**: Toda Unidad Organizacional (UO) debe tener la política de verificación en 2 pasos activada como **Obligatoria**.
2. **Principio de Mínimo Privilegio**: No otorgar roles de Super Administrador para labores operativas. Utilizar roles delegados por UO.
3. **Mapeo Riguroso de Dominios Alias**: Al agregar un Dominio Alias de Usuario, todo usuario cuyo nombre difiera del prefijo principal debe registrarse explícitamente como alias alternativo en su perfil para evitar rebotes `550 5.1.1 NoSuchUser`.

---

## 2. Reglas de DNS, Enrutamiento y Cero Pérdida de Correo

1. **Tríada Criptográfica Obligatoria**:
   - **SPF**: Todo dominio debe tener un único registro TXT SPF que autorice a `_spf.google.com` y a las IPs públicas de aplicaciones web emisoras.
   - **DKIM**: Clave RSA 2048-bit generada en la consola y publicada en DNS (`google._domainkey`).
   - **DMARC**: Registro `_dmarc` con política `p=quarantine` o `p=reject` y buzón de reportes `rua`.
2. **Regla de Contingencia Catch-All**:
   - Todo dominio alias debe contar con una regla de enrutamiento predeterminado (*Default Routing*) aplicada **exclusivamente a direcciones no reconocidas** que redirija a Administración con prefijo identificador (`[Dominio Histórico]`).
3. **Intercambiador Remoto en cPanel**:
   - Cuando un servidor web comparta el dominio con Google Workspace, el *Email Routing* en cPanel debe estar configurado como **Remote Mail Exchanger**.

---

## 3. Reglas de Unidades Compartidas y DLP

1. **Restricción de Descarga e Impresión**: Las Unidades Compartidas con información pericial, legal, médica o financiera deben tener activada la opción *"Impedir que lectores y comentaristas descarguen, impriman o copien archivos"*.
2. **Control de Aplicaciones de Terceros**: Las APIs de Gmail y Drive solo deben autorizar aplicaciones validadas en la lista blanca (*Allowlist*).

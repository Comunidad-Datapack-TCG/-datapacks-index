# Política de Privacidad

**FiguFC 27**  
**Desarrollador / Empresa:** TapGoal Studios  
**Identificador de la aplicación (Package Name):** `com.tapgaolstudios.figufc`  
**Última actualización:** 25 de octubre de 2026  
**Fecha de entrada en vigor:** 25 de octubre de 2026  

---

## 1. Quiénes somos y alcance de esta política
**FiguFC 27** («la aplicación», «el juego», «nuestro servicio») es un videojuego móvil de coleccionismo de cartas, simulación deportiva, Squad Draft y gestión futbolística desarrollado, publicado y operado por **TapGoal Studios** («nosotros», «nuestro», «el desarrollador»).

Esta Política de Privacidad detalla nuestras prácticas relativas a la recopilación, almacenamiento, uso, protección, divulgación y eliminación de la información personal y técnica de los usuarios («el usuario», «tú») que descargan, instalan o interactúan con **FiguFC 27** a través de Google Play Store.

Este documento ha sido redactado en estricto cumplimiento de:
- Las **Políticas del Programa para Desarrolladores de Google Play** (incluyendo los requisitos de la sección de Seguridad de los Datos / *Data Safety* y la política obligatoria de eliminación de cuentas).
- El **Reglamento General de Protección de Datos de la Unión Europea (GDPR / RGPD)**.
- La **Ley de Privacidad del Consumidor de California (CCPA / CPRA)**.
- La **Ley de Protección de la Privacidad Infantil en Internet (COPPA)**.

Al descargar, acceder o utilizar **FiguFC 27**, aceptas las prácticas descritas en esta Política de Privacidad. Si no estás de acuerdo con estos términos, te solicitamos no utilizar la aplicación.

---

## 2. Información que recopilamos
En **FiguFC 27** aplicamos el principio de minimización de datos: recopilamos única y exclusivamente los datos técnicos y de cuenta indispensables para proporcionar la experiencia de juego, garantizar el guardado en la nube, procesar compras legítimas y desplegar publicidad recompensada.

A continuación, detallamos las categorías de datos recopilados conforme a las especificaciones de Google Play:

### A. Información personal y de cuenta
- **Identificador de usuario (User ID):** Se genera un identificador anónimo único mediante Firebase Authentication para asociar tu inventario de cartas, monedas y progreso sin obligarte a registrar datos personales.
- **Nombre y correo electrónico (Opcional - Inicio de sesión con Google):** Si decides vincular voluntariamente tu cuenta mediante Google Play Games o Google Sign-In, recibimos tu nombre público de jugador y tu dirección de correo electrónico vinculada. Estos datos se utilizan únicamente para autenticar tu sesión, sincronizar tu progreso en la nube y permitir la recuperación de tu cuenta en otros dispositivos.
- **Foto de perfil o avatar:** Si configuras un avatar personalizado o utilizas la foto de tu cuenta pública de Google, dicha imagen se procesa únicamente para mostrar tu perfil dentro del juego y en las salas de emparejamiento multijugador.

### B. Identificadores de dispositivo y publicidad
- **Identificador del dispositivo / UUID de instalación:** Un identificador criptográfico anónimo generado en el primer inicio de la app para gestionar la sesión local y el guardado sin conexión.
- **Identificador de Publicidad de Google (Google Advertising ID / GAID / AAID):** Recopilado de forma automática por el SDK de **Google AdMob** con fines de visualización de anuncios publicitarios, prevención de fraudes y atribución analítica.

### C. Actividad y progreso en el juego
- **Estadísticas de juego:** Progreso en Modo Carrera, cartas desbloqueadas en álbumes, plantillas activas de Squad Draft, puntos en Liga de Divisiones Online, historial de partidos y registros en el podio de clasificación.
- **Interacciones con el mercado y vitrinas:** Publicaciones realizadas en el mercado de cartas e historial de intercambios sociales dentro del juego.

### D. Información financiera y compras integradas (*In-App Purchases*)
- **Historial de transacciones de Google Play:** Cuando compras artículos virtuales (como sobres de cartas o monedas virtuales), la transacción es procesada íntegra y exclusivamente por el sistema oficial **Google Play Billing** (Google LLC).
- **Lo que NO recopilamos:** **TapGoal Studios** **NUNCA** recopila, almacena, procesa ni tiene acceso a números de tarjetas de crédito/débito, cuentas bancarias ni credenciales de pago. Solo recibimos confirmaciones criptográficas de compra (tokens de recibo y Order IDs anónimos) emitidas por Google Play para acreditar los artículos digitales a tu inventario.

### E. Diagnósticos y rendimiento técnico
- **Registros de errores y fallos (*Crash Logs*):** Información técnica del sistema operativo (versión de Android, modelo del dispositivo, memoria disponible y traza del error en caso de cierre inesperado) utilizada exclusivamente para depurar errores y mejorar la estabilidad del juego.

---

## 3. Finalidades y bases legales del tratamiento
De conformidad con las normativas internacionales de protección de datos (como el RGPD), tratamos tu información bajo las siguientes bases legales y finalidades:

| Categoría de dato | Finalidad principal | Base legal (RGPD / Normativa) |
| :--- | :--- | :--- |
| **Identificador de dispositivo / User ID** | Funcionamiento básico de la app, guardado local y en la nube de partidas, inventario de cartas y monedas. | Ejecución del servicio / Contrato |
| **Nombre y correo electrónico** | Autenticación mediante Google, recuperación de cuenta en múltiples dispositivos y atención a solicitudes de soporte. | Consentimiento explícito del usuario |
| **Foto de perfil** | Personalización estética del perfil y visualización en clasificaciones y partidos multijugador. | Consentimiento explícito del usuario |
| **Google Advertising ID (GAID)** | Despliegue de anuncios recompensados (obtención de sobres y recompensas gratis) y análisis de rendimiento publicitario. | Interés legítimo / Consentimiento (EEA) |
| **Datos de actividad en el juego** | Balance de cartas, cálculo de puntuaciones en Draft, emparejamiento justo (PvP) y prevención de trampas (*anti-cheat*). | Interés legítimo / Ejecución del servicio |
| **Tokens de compra (Google Play)** | Verificación y entrega legítima de productos digitales y monedas adquiridas. | Cumplimiento contractual y obligación legal |
| **Registros de fallos y diagnóstico** | Detección de errores, corrección de bugs y optimización del rendimiento en diversos dispositivos Android. | Interés legítimo |

---

## 4. Terceros y proveedores de servicios autorizados
**TapGoal Studios no vende, alquila ni comercializa datos personales de los usuarios bajo ninguna circunstancia.**

Para prestar nuestros servicios, integramos SDKs y tecnologías de proveedores líderes que cumplen con estrictos estándares de seguridad y normativas internacionales de privacidad:

1. **Google Firebase (Google LLC):**
   - **Servicios empleados:** Firebase Authentication (autenticación segura), Cloud Firestore (almacenamiento de base de datos en tiempo real) y Cloud Storage (almacenamiento en la nube).
   - **Finalidad:** Sincronización de progreso, cartas, amigos y clasificaciones.
   - **Política de privacidad:** [https://policies.google.com/privacy](https://policies.google.com/privacy) | [https://firebase.google.com/support/privacy](https://firebase.google.com/support/privacy)

2. **Google AdMob (Google LLC):**
   - **Servicios empleados:** Red de publicidad móvil.
   - **Finalidad:** Monetización del juego mediante anuncios de video recompensado (para ganar sobres y fichas) y banners.
   - **Política de publicidad de Google:** [https://policies.google.com/technologies/ads](https://policies.google.com/technologies/ads)

3. **Google Play Services y Google Play Billing (Google LLC):**
   - **Servicios empleados:** Facturación integrada, logros y servicios de juegos.
   - **Finalidad:** Procesamiento seguro de pagos y entrega de artículos virtuales.
   - **Términos de servicio de Google Play:** [https://play.google.com/intl/es_es/about/play-terms/](https://play.google.com/intl/es_es/about/play-terms/)

Todos estos proveedores cuentan con certificaciones internacionales de seguridad y mecanismos de transferencia legal de datos (como las Cláusulas Contractuales Tipo de la Comisión Europea).

---

## 5. Publicidad y control del usuario
**FiguFC 27** es un juego gratuito financiado en parte mediante anuncios provistos por **Google AdMob**.

### Control de anuncios personalizados en tu dispositivo Android
Puedes en cualquier momento consultar, restablecer o eliminar tu Identificador de Publicidad desde la configuración de tu teléfono móvil:
1. Abre los **Ajustes / Configuración** de tu dispositivo Android.
2. Ve a **Google** (o **Servicios de Google**).
3. Selecciona **Anuncios**.
4. Pulsa en **«Restablecer ID de publicidad»** o **«Borrar ID de publicidad»**.

### Usuarios en la Unión Europea / Espacio Económico Europeo (EEE) y Reino Unido
En cumplimiento con la Política de Consentimiento de Usuarios de la UE de Google y el RGPD, los usuarios en regiones reguladas tienen acceso al cuadro de diálogo de consentimiento (CMP / UMP SDK) donde pueden elegir si aceptan o rechazan anuncios personalizados y tecnologías de seguimiento.

---

## 6. Privacidad de los menores (COPPA y Familias)
**FiguFC 27** está diseñado para una audiencia general y es apto para todas las edades; sin embargo, **no está dirigido deliberadamente a niños menores de 13 años** (o menores de 16 años en jurisdicciones de la Unión Europea).

- No recopilamos conscientemente información personal identificable de menores de 13 años sin el consentimiento previo y verificable de sus padres o tutores legales.
- Si eres padre, madre o tutor legal y tienes conocimiento de que tu hijo menor nos ha facilitado información personal sin tu consentimiento, ponte en contacto con nosotros de inmediato en [futbolen570@gmail.com](mailto:futbolen570@gmail.com). Procederemos a investigar y eliminar dicha información de nuestros servidores a la mayor brevedad posible.

---

## 7. Retención y conservación de los datos
Conservamos los datos de los usuarios únicamente durante el tiempo necesario para cumplir las finalidades descritas en esta política:
- **Datos de cuenta y progreso:** Se conservan mientras tu cuenta permanezca activa. Si una cuenta vinculada permanece inactiva por más de 24 meses consecutivos, nos reservamos el derecho de purgar registros temporales.
- **Comprobantes y recibos de compras:** Se conservan durante los plazos legalmente exigidos por las normativas fiscales, contables y de prevención de fraudes comerciales aplicables a transacciones digitales de Google Play.
- **Datos eliminados a petición:** Una vez solicitada la eliminación de la cuenta conforme a la Sección 8, los datos son borrados o anonimizados irreversiblemente en un plazo máximo de treinta (30) días.

---

## 8. Eliminación de cuentas y derechos sobre tus datos (Requisito obligatorio de Google Play)
En cumplimiento estricto con las directrices de Google Play sobre la eliminación de cuentas y datos del usuario, garantizamos que puedes solicitar la eliminación permanente de tu cuenta y todos sus datos asociados, **tanto desde dentro del juego como de manera externa por correo electrónico / web**:

### Opción 1: Eliminación directa desde el juego
1. Abre **FiguFC 27**.
2. Dirígete a la pantalla de **Ajustes** (icono de engranaje).
3. En la sección de **Cuenta**, selecciona **«Desvincular Cuenta»** o pulsa en **«Eliminar mi cuenta y datos»**.
4. Confirma la acción en el cuadro de diálogo.

### Opción 2: Solicitud externa por correo electrónico (sin necesidad de tener la app instalada)
Si has desinstalado el juego o deseas solicitar la eliminación completa de tus datos de manera remota:
1. Envía un correo electrónico a nuestra casilla oficial de soporte: **[futbolen570@gmail.com](mailto:futbolen570@gmail.com)**.
2. En el asunto escribe: `Solicitud de Eliminación de Cuenta - FiguFC 27`.
3. En el mensaje, incluye el correo de Google con el que vinculaste tu cuenta o tu nombre público de usuario / ID de jugador.
4. Nuestro equipo procesará tu solicitud y confirmará la eliminación definitiva en un plazo no mayor a **30 días hábiles**.

### ¿Qué datos se eliminan de manera definitiva?
- Tu perfil de jugador, correo electrónico y credenciales en Firebase Authentication.
- Tu inventario de cartas, monedas, álbumes completados y plantillas de Squad Draft.
- Tu historial de partidos, calificaciones en Liga de Divisiones y récords en el Ranking.
- Tu lista de amigos, ofertas del mercado y mensajes de intercambio.

*(Nota: Los registros de facturación de compras de Google Play se archivan de forma anonimizada únicamente por obligación legal y auditoría contable).*

---

## 9. Derechos del usuario según normativas globales (RGPD / CCPA)
De acuerdo con las leyes aplicables de protección al consumidor y privacidad, gozas de los siguientes derechos fundamentales:
- **Derecho de Acceso:** Solicitar una copia comprensible de los datos personales que conservamos sobre ti.
- **Derecho de Rectificación:** Solicitar la corrección de datos inexactos o incompletos.
- **Derecho de Supresión («Derecho al Olvido»):** Solicitar el borrado total de tus datos personales conforme a la Sección 8.
- **Derecho a la Portabilidad:** Recibir tus datos en un formato estructurado y de uso común.
- **Derecho de Oposición y Limitación:** Oponerte al tratamiento de tus datos o restringir determinados procesamientos técnicos.
- **Derecho a la No Discriminación:** No recibirás ningún trato discriminatorio por ejercer tus derechos de privacidad.

Para ejercer cualquiera de estos derechos, contáctanos en [futbolen570@gmail.com](mailto:futbolen570@gmail.com). Responderemos a tu solicitud en los plazos establecidos por la ley.

---

## 10. Seguridad de la información
En **TapGoal Studios** nos tomamos muy en serio la seguridad de tu información:
- Todas las comunicaciones y transferencias de datos entre **FiguFC 27** y nuestros servidores en la nube se realizan mediante canales cifrados utilizando protocolos estándar **HTTPS / TLS 1.2+**.
- Los datos se almacenan en la infraestructura de alta seguridad de **Google Cloud Platform / Firebase**, protegida por cortafuegos, autenticación multifactor, cifrado en reposo y monitoreo continuo contra accesos no autorizados.

A pesar de nuestros esfuerzos y la adopción de las mejores prácticas de la industria, ningún método de transmisión por Internet o almacenamiento electrónico es 100% infalible; no obstante, garantizamos que aplicamos todas las medidas técnicas razonables y proporcionales para mitigar cualquier riesgo.

---

## 11. Cambios a esta Política de Privacidad
Nos reservamos el derecho de actualizar o modificar esta Política de Privacidad para reflejar cambios normativos, mejoras en las funciones de **FiguFC 27** o nuevos requerimientos de Google Play Store.

- Cualquier cambio entrará en vigor inmediatamente tras la publicación de la versión actualizada.
- Indicaremos siempre la fecha de **«Última actualización»** en el encabezado de este documento.
- Si implementamos cambios sustanciales que afecten el modo en que tratamos tus datos personales, publicaremos un aviso destacado dentro de la aplicación antes de que dichos cambios entren en vigencia.

Te recomendamos revisar periódicamente esta página para mantenerte informado sobre cómo protegemos tu información.

---

## 12. Información de contacto oficial
Si tienes preguntas, dudas, comentarios o deseas ejercer tus derechos de privacidad o eliminación de datos respecto a **FiguFC 27**, puedes comunicarte directamente con nosotros:

- **Empresa / Desarrollador:** TapGoal Studios  
- **Aplicación:** FiguFC 27  
- **Identificador de paquete (Package ID):** `com.tapgaolstudios.figufc`  
- **Sitio web oficial / Portal de políticas:** [https://comunidad-datapack-tcg.github.io/-datapacks-index/privacy-policy](https://comunidad-datapack-tcg.github.io/-datapacks-index/privacy-policy)  
- **Correo electrónico de soporte y privacidad:** **[futbolen570@gmail.com](mailto:futbolen570@gmail.com)**  

---
*© 2026 TapGoal Studios. Todos los derechos reservados.*

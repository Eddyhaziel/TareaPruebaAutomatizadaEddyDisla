# Historias de Usuario

## 1. Login en la aplicación

- **Historia de Usuario**: Como usuario registrado, quiero iniciar sesión con mi correo electrónico y contraseña para acceder a mi cuenta.
- **Criterios de Aceptación**:
  - El formulario de login debe aceptar un correo electrónico y una contraseña.
  - Al ingresar las credenciales correctas, el usuario debe ser redirigido a la página principal.
- **Criterios de Rechazo**:
  - Si las credenciales son incorrectas, se debe mostrar un mensaje de error.
  - Si el campo de correo electrónico está vacío, debe aparecer un mensaje de advertencia.

## 2. Agregar producto al carrito

- **Historia de Usuario**: Como comprador, quiero agregar productos a mi carrito para poder realizar una compra más tarde.
- **Criterios de Aceptación**:
  - Al hacer clic en el botón "Agregar al carrito", el producto debe ser agregado al carrito.
  - El número de productos en el carrito debe reflejarse correctamente.
- **Criterios de Rechazo**:
  - Si el botón "Agregar al carrito" no funciona, el producto no debe ser agregado al carrito.
  - Si el carrito está vacío, debe mostrar un mensaje "Carrito vacío".

## 3. Visualización de productos en la tienda

- **Historia de Usuario**: Como usuario, quiero ver los productos disponibles en la tienda para poder elegir el que deseo comprar.
- **Criterios de Aceptación**:
  - Todos los productos disponibles deben mostrarse en la página de inicio.
  - Cada producto debe mostrar su imagen, precio y nombre.
- **Criterios de Rechazo**:
  - Si algún producto no se carga, debe aparecer un mensaje indicando que no está disponible.

## 4. Validación de campo de email en formulario

- **Historia de Usuario**: Como usuario, quiero que el campo de email en el formulario se valide correctamente para asegurarme de que mi correo es correcto.
- **Criterios de Aceptación**:
  - El campo de email debe aceptar solo direcciones de correo electrónico válidas.
  - Si el formato del email es incorrecto, debe mostrarse un mensaje de error.
- **Criterios de Rechazo**:
  - Si el correo electrónico está vacío o tiene un formato incorrecto, no debe enviarse el formulario.

## 5. Buscar producto en la barra de búsqueda

- **Historia de Usuario**: Como usuario, quiero buscar productos usando la barra de búsqueda para encontrar rápidamente lo que estoy buscando.
- **Criterios de Aceptación**:
  - La barra de búsqueda debe aceptar texto y devolver productos relevantes.
  - Los resultados deben mostrarse de forma clara y ordenada.
- **Criterios de Rechazo**:
  - Si no hay resultados, debe mostrarse un mensaje indicando que no se encontraron productos.

## 6. Registro de nuevo usuario

- **Historia de Usuario**: Como nuevo usuario, quiero registrarme en la aplicación utilizando mi correo electrónico y una contraseña para crear una cuenta y poder acceder a las funciones del sitio.
- **Criterios de Aceptación**:
  - El formulario de registro debe aceptar un correo electrónico y una contraseña.
  - El correo electrónico debe ser único, es decir, no debe estar registrado previamente.
  - Al completar el registro, el usuario debe recibir un mensaje de confirmación de éxito.
- **Criterios de Rechazo**:
  - Si el correo electrónico ya está registrado, debe mostrarse un mensaje indicando que la cuenta ya existe.
  - Si los campos del formulario están vacíos, debe mostrarse un mensaje de advertencia.

## 7. Filtrar productos por categoría

- **Historia de Usuario**: Como usuario, quiero poder filtrar los productos por categorías (por ejemplo, apartamentos, casas, terrenos) para encontrar fácilmente lo que busco.
- **Criterios de Aceptación**:
  - El usuario debe poder seleccionar una categoría de productos.
  - Al seleccionar una categoría, solo los productos de esa categoría deben mostrarse.
  - Los filtros deben ser claros y fáciles de usar.
- **Criterios de Rechazo**:
  - Si no hay productos en la categoría seleccionada, debe mostrarse un mensaje "No se encontraron productos en esta categoría".
  - Si el filtro no aplica correctamente, se debe mostrar un mensaje de error.

## 8. Visualización del detalle del producto

- **Historia de Usuario**: Como usuario, quiero ver el detalle completo de un producto, incluyendo imágenes adicionales, descripción, ubicación y precio, para poder tomar una decisión informada sobre la compra.
- **Criterios de Aceptación**:
  - Al hacer clic en un producto, el usuario debe ser redirigido a una página con más detalles del producto.
  - La página de detalles debe mostrar imágenes adicionales, una descripción detallada, ubicación y el precio del producto.
- **Criterios de Rechazo**:
  - Si no hay detalles disponibles, debe mostrarse un mensaje indicando que no hay información adicional disponible.

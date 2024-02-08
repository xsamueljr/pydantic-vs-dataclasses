Ejercicio de prueba de validación de datos con Pydantic y dataclasses.

Ambos modelos son iguales, y en cada test se prueban ambos, pues se espera el mismo comportamiento. Sus campos son:
- `email`. Email del usuario. Se valida que sea una dirección de correo válida.
- `password`. Contraseña del usuario. Se valida que cumpla todos los requisitos establecidos, que son los siguientes:
   - Debe tener de 8 a 16 caracteres.
   - Debe tener mínimo 1 número, 1 mayúscula, 1 minúscula y 1 caracter especial.
   - No puede ser un palíndromo (Es decir, que no se lee igual cuando le das la vuelta).
   - No puede tener espacios en blanco.

La validación del email en Pydantic es automática gracias a `EmailStr`, y en dataclasses la he implementado usando una expresión regular. Luego, toda la lógica de validación para la contraseña está en un módulo aparte. Ambos modelos lo usan.
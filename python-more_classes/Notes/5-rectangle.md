# Notas sobre la clase Rectangle

```markdown
### El atributo de clase **number_of_instances** se utiliza para llevar un conteo de cuántas instancias (objetos) de una clase se han creado y eliminado. Aquí te detallo cómo funciona:
```markdown

## Inicialización
- `number_of_instances` se inicializa en 0. Esto significa que, al principio, no hay instancias de la clase.

## Incremento
- Cada vez que se crea una nueva instancia de la clase, `number_of_instances` se incrementa en 1. Esto se hace típicamente en el constructor de la clase (el método `__init__` en Python).

## Decremento
- Cada vez que se elimina una instancia de la clase, `number_of_instances` se decrementa en 1. Esto se puede hacer en el método destructor de la clase (el método `__del__` en Python).
```

### Argumentación
1. **Encabezados**: Se añadieron encabezados para organizar mejor la información.
2. **Código en línea**: Se utilizaron backticks (\`) para resaltar los nombres de métodos y variables como código.
3. **Formato**: Se mejoró la legibilidad del texto con listas y secciones claras.
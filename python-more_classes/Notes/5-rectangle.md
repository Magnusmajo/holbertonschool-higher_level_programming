# Notas sobre la clase Rectangle

```markdown
### El atributo de clase `number_of_instances` se utiliza para llevar un conteo de cuántas instancias (objetos) de una clase se han creado y eliminado.

### Cómo funciona?

## Inicialización
- `number_of_instances` se inicializa en 0. Esto significa que, al principio, no hay instancias de la clase.

## Incremento
- Cada vez que se crea una nueva instancia de la clase, `number_of_instances` se incrementa en 1. Esto se hace típicamente en el constructor de la clase (el método `__init__` en Python).

## Decremento
- Cada vez que se elimina una instancia de la clase, `number_of_instances` se decrementa en 1. Esto se puede hacer en el método destructor de la clase (el método `__del__` en Python).

### Argumentación

El uso del atributo de clase `number_of_instances` es crucial para el  
manejo eficiente de recursos y la depuración en aplicaciones complejas.  
Al mantener un registro preciso del número de instancias activas, los  
desarrolladores pueden identificar fácilmente posibles fugas de memoria  
y optimizar el uso de recursos. Además, este conteo puede ser útil para  
implementar patrones de diseño como el Singleton, donde se necesita  
controlar estrictamente el número de instancias de una clase. En resumen,  
`number_of_instances` no solo facilita el seguimiento de objetos, sino que  
también contribuye a la estabilidad y eficiencia del software.
```
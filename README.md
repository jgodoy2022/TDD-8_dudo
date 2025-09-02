# Cacho/Dudo Test Driven Development
Implementación del juego Dudo/Cacho usando la metodologia Test Driven Development (TDD) (Grupo 8)
### Integrantes
- Felipe Mendoza
- Joaquín Godoy
- Marcelo Vergara

# Instalación
### Clona el repositorio:
```git
git clone https://github.com/jgodoy2022/TDD-8_dudo.git
```
### Instalación de dependencias
El proyecto fue desarrollado utilizando Python 3.12.7

En el directorio raíz se encuentra el archivo requirements.txt el cual posee las dependencias utilizadas en el proyecto, lo emplearemos para instalarlas dentro de un entorno virtual que deberás crear.

Una vez creado, se debe activar el entorno virtual, dejar el archivo requirements.txt dentro de este, y ejecutar el siguiente comando:
```bash
pip install -r requirements.txt
```
Con esto ya estarán todas las dependencias de testing necesarias para el proyecto.

### Testing
Para correr los tests hay que ejecutar el siguiente comando en el directorio raiz.

```bash
python -m pytest  
```

### Coverage
Para correr la cobertura del proyecto hay que ejecutar el siguiente comando en el directorio raiz.

```bash
.\run_coverage.ps1
```
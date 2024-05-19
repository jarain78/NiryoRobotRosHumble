# Niryo Robot ROS 2 Humble


# Visualización del Brazo Niryo 2 con ROS 2 Humble

Este repositorio proporciona una visualización detallada del brazo robótico Niryo 2 utilizando ROS 2 Humble. A continuación, se detallan las instrucciones para lanzar el proyecto y visualizar el funcionamiento del brazo robótico.


![Descripción de la imagen](media/3074021.jpeg)


## Introducción

El proyecto está diseñado para mostrar cómo se puede utilizar ROS 2 Humble para controlar y visualizar el brazo robótico Niryo 2. ROS 2 (Robot Operating System) es un conjunto de bibliotecas y herramientas que ayudan a los desarrolladores a crear aplicaciones robóticas. Esta versión, Humble Hawksbill, introduce mejoras en la comunicación entre nodos, control del robot y herramientas de simulación.

## Prerrequisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados en tu sistema:

- **Ubuntu 22.04** (recomendado para compatibilidad completa con ROS 2 Humble)
- **ROS 2 Humble Hawksbill**: Puedes seguir las instrucciones de instalación oficiales en [ROS 2 Humble Installation](https://docs.ros.org/en/humble/Installation.html).
- **Niryo One ROS 2 Packages**: Asegúrate de clonar los paquetes necesarios desde el repositorio oficial de Niryo One.
- **rviz2**: Una herramienta de visualización 3D para ROS 2.

## Instalación

Sigue estos pasos para configurar tu entorno y clonar el repositorio:

1. **Instalar ROS 2 Humble**:

    ```sh
    sudo apt update
    sudo apt install ros-humble-desktop
    ```

2. **Configurar el espacio de trabajo de ROS 2**:

    ```sh
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ```

3. **Clonar este repositorio**:

    ```sh
    https://github.com/jarain78/NiryoRobotRosHumble.git
    cd ..
    rosdep install --from-paths src --ignore-src -r -y
    ```

4. **Compilar el espacio de trabajo**:

    ```sh
    colcon build
    ```

5. **Fuente el espacio de trabajo**:

    ```sh
    source install/setup.bash
    ```

## Lanzamiento del Proyecto

Para iniciar la visualización del brazo Niryo 2, utiliza el siguiente comando:

```sh
ros2 launch test_niryo_v3 slider_control.launch.py
```

Este comando lanzará los nodos necesarios y abrirá `rviz2` con la configuración adecuada para visualizar el brazo Niryo 2 en un entorno 3D.

![Descripción de la imagen](media/NiryoOne.png)

## Uso

Una vez que el proyecto esté en funcionamiento, puedes interactuar con el brazo Niryo 2 a través de la interfaz de `rviz2`. Puedes realizar las siguientes acciones:

- **Controlar el movimiento del brazo**: Utiliza los plugins de ROS 2 para enviar comandos de movimiento.
- **Visualizar el estado del brazo**: Monitorea la posición, orientación y estado de las articulaciones del brazo en tiempo real.
- **Simulaciones**: Realiza simulaciones para probar diferentes algoritmos de control y planificación de trayectorias.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si tienes mejoras, correcciones o nuevas funcionalidades que te gustaría añadir, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits descriptivos.
4. Envía un pull request detallado explicando tus cambios.

## Soporte

Si encuentras algún problema o tienes preguntas sobre el uso de este repositorio, por favor abre un issue en GitHub. También puedes contactar a los mantenedores del proyecto a través del correo electrónico [jarincon@ubu.es](mailto:soporte@ejemplo.com).

---

Esto proporciona una guía más detallada y profesional para los usuarios que deseen utilizar y contribuir al proyecto.
    






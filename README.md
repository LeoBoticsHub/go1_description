# go1_description

This package contains the go1 description files. It works both with ROS and ROS 2 distros.

## Dependencies

this package depends on the following:

* [sensors_description](https://github.com/LeoBoticsHub/sensors_description.git)
* velodyne_description ```sudo apt install ros-$ROS_DISTRO-velodyne-description```

please clone it in the same workspace of go1_description.

## Launch files

To see the robot description on rviz and interact with it:

* ROS:

```bash
roslaunch go1_description go1_rviz.launch sensors:=true
```

* ROS 2:

```bash
ros2 launch go1_description go1_rviz.launch.py
```

To upload robot description and start robot state publisher for rviz visualization purposes in real applications:

* ROS:

```bash
roslaunch go1_description upload.launch sensors:=true
```

* ROS 2:

```bash
ros2 launch go1_description upload.launch.py
```

To automatically launch RViz, launch:

```bash
ros2 launch go1_description upload.launch.py use_rviz:=true
```

by default `use_rviz:=true` is `false`.

## Environment

We recommand users to run this package in Ubuntu 20.04 or 22.04 and ROS noetic, Foxy or Humble environment.

## Authors

The package is provided by:

* [Federico Rollo](https://github.com/FedericoRollo) [Mantainer]
* [Valentina Pericu](https://github.com/valeperi) [Mantainer]
from laspy import read
from numpy import sqrt, vstack, linspace
from open3d import geometry, utility, visualization
import numpy as np
import os

input_path=os.getcwd() + '/'  #path to folder
dataname="aircraft.las" #point cloud name 

point_cloud = read(input_path + dataname) 
pcd = geometry.PointCloud()
pcd.points = utility.Vector3dVector(vstack((point_cloud.x,
                                            point_cloud.y,
                                            point_cloud.z)
                                           ).transpose())

pcd.colors = utility.Vector3dVector(vstack((point_cloud.red, 
                                               point_cloud.green,
                                               point_cloud.blue)
                                    ).transpose() / 65535)
pcd.estimate_normals()
v_size = 0.15
voxel_grid = geometry.VoxelGrid.create_from_point_cloud(pcd,
             voxel_size=v_size)

visualization.draw_geometries([voxel_grid])


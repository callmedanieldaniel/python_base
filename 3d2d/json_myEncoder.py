#coding:utf-8
'''
Created
'''

import numpy as np

def bbox3d_lidar2cam(corners, RT_cam2lidar, Intrinsic_cam):
    assert len(corners.shape)==2 and corners.shape[0]==8,"points.shape must=(8,3)"
    points_homo=np.hstack((corners,np.ones((len(corners),1))))
    R=RT_cam2lidar[0:3,0:3]
    T=RT_cam2lidar[0:3,3:4]
    RT_lidar2cam=np.zeros((4,4))
    RT_lidar2cam[0:3,0:3]=np.linalg.inv(R)
    RT_lidar2cam[0:3,3:4]=-1*np.matmul(np.linalg.inv(R), T)
    RT_lidar2cam[3,3]=1.0

    RT_cam2image = np.array(Intrinsic_cam).reshape(3, 3)
    # R_Cam2Cam=np.array([[0,-1,0], [0,0,-1], [1,0,0.]])
    R_Cam2Cam=np.array([[1,0,0], [0,1,0], [0,0,1.]])
    points_top_homo_cam=np.matmul(RT_lidar2cam,points_homo.T).T[:,0:3]
    points_top_homo_cam=np.matmul(R_Cam2Cam,points_top_homo_cam.T).T
    points_top_homo_img=np.matmul(RT_cam2image,points_top_homo_cam.T).T
    points_top_homo_img=np.divide(points_top_homo_img,points_top_homo_cam[:,2:3])[:,0:2]

    return points_top_homo_img

def ROI_Frustm(bbox2d, RT_cam2lidar,Intrinsic_cam, distance=200):
    assert len(bbox2d.shape)==1 and bbox2d.shape[0]==4,"bbox2d.shape must=(4)"
    def inverse(RT_cam2lidar):
        R = RT_cam2lidar[0:3, 0:3]
        T = RT_cam2lidar[0:3, 3:4]
        RT_lidar2cam = np.zeros((4, 4))
        RT_lidar2cam[0:3, 0:3] = np.linalg.inv(R)
        RT_lidar2cam[0:3, 3:4] = -1 * np.matmul(np.linalg.inv(R), T)
        RT_lidar2cam[3, 3] = 1.0
        return RT_lidar2cam

    R=RT_cam2lidar[0:3,0:3]
    T=RT_cam2lidar[0:3,3:4]
    RT_lidar2cam=np.zeros((4,4))
    RT_lidar2cam[0:3,0:3]=np.linalg.inv(R)
    RT_lidar2cam[0:3,3:4]=-1*np.matmul(np.linalg.inv(R), T)
    RT_lidar2cam[3,3]=1.0

    RT_cam2image=np.array(Intrinsic_cam).reshape(3,3)
    # R_Cam2Cam=np.array([[0,-1,0], [0,0,-1], [1,0,0.]])
    R_Cam2Cam=np.array([[1,0,0], [0,1,0], [0,0,1.]])


    points_top_homo_img=np.array([[bbox2d[0],bbox2d[1],1.0],
                                  [bbox2d[0],bbox2d[3],1.0],
                                  [bbox2d[2],bbox2d[3],1.0],
                                  [bbox2d[2],bbox2d[1],1.0]], dtype=np.float)

    points_top_homo=points_top_homo_img*float(distance)
    points_top_homo_cam=np.matmul(np.linalg.inv(RT_cam2image),points_top_homo.T).T
    points_homo=np.matmul(np.linalg.inv(R_Cam2Cam),points_top_homo_cam.T).T
    points_homo = np.hstack((points_homo, np.ones((len(points_homo), 1))))
    # points_top_homo_lidar=np.matmul(inverse(RT_lidar2cam),points_homo.T).T[:,0:3]
    points_top_homo_lidar=np.matmul(RT_cam2lidar,points_homo.T).T[:,0:3]

    points_top_homo=points_top_homo_img*float(0.01)
    points_top_homo_cam=np.matmul(np.linalg.inv(RT_cam2image),points_top_homo.T).T
    points_homo=np.matmul(np.linalg.inv(R_Cam2Cam),points_top_homo_cam.T).T
    points_homo = np.hstack((points_homo, np.ones((len(points_homo), 1))))
    # points_top_homo_lidar=np.matmul(inverse(RT_lidar2cam),points_homo.T).T[:,0:3]
    points_top_homo_lidar2=np.matmul(RT_cam2lidar,points_homo.T).T[:,0:3]

    points=np.vstack([points_top_homo_lidar2,points_top_homo_lidar])

    return points

def bbox3d_lidar2cam(corners, RT_cam2lidar, Intrinsic_cam):
    assert len(corners.shape)==2 and corners.shape[0]==8,"points.shape must=(8,3)"
    points_homo=np.hstack((corners,np.ones((len(corners),1))))
    R=RT_cam2lidar[0:3,0:3]
    T=RT_cam2lidar[0:3,3:4]
    RT_lidar2cam=np.zeros((4,4))
    RT_lidar2cam[0:3,0:3]=np.linalg.inv(R)
    RT_lidar2cam[0:3,3:4]=-1*np.matmul(np.linalg.inv(R), T)
    RT_lidar2cam[3,3]=1.0

    RT_cam2image = np.array(Intrinsic_cam).reshape(3, 3)
    # R_Cam2Cam=np.array([[0,-1,0], [0,0,-1], [1,0,0.]])
    R_Cam2Cam=np.array([[1,0,0], [0,1,0], [0,0,1.]])
    points_top_homo_cam=np.matmul(RT_lidar2cam,points_homo.T).T[:,0:3]
    points_top_homo_cam=np.matmul(R_Cam2Cam,points_top_homo_cam.T).T
    points_top_homo_img=np.matmul(RT_cam2image,points_top_homo_cam.T).T
    points_top_homo_img=np.divide(points_top_homo_img,points_top_homo_cam[:,2:3])[:,0:2]

    return points_top_homo_img


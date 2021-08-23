# coding:utf-8
'''
Created
'''
import numpy as np

def ROI_Frustm(bbox2d, RT_cam2lidar, Intrinsic_cam, distance=200):
    assert len(bbox2d.shape) == 1 and bbox2d.shape[0] == 4, "bbox2d.shape must=(4)"

    def inverse(RT_cam2lidar):
        R = RT_cam2lidar[0:3, 0:3]
        T = RT_cam2lidar[0:3, 3:4]
        RT_lidar2cam = np.zeros((4, 4))
        RT_lidar2cam[0:3, 0:3] = np.linalg.inv(R)
        RT_lidar2cam[0:3, 3:4] = -1 * np.matmul(np.linalg.inv(R), T)
        RT_lidar2cam[3, 3] = 1.0
        return RT_lidar2cam

    R = RT_cam2lidar[0:3, 0:3]
    T = RT_cam2lidar[0:3, 3:4]
    RT_lidar2cam = np.zeros((4, 4))
    RT_lidar2cam[0:3, 0:3] = np.linalg.inv(R)
    RT_lidar2cam[0:3, 3:4] = -1 * np.matmul(np.linalg.inv(R), T)
    RT_lidar2cam[3, 3] = 1.0

    RT_cam2image = np.array(Intrinsic_cam).reshape(3, 3)
    # R_Cam2Cam=np.array([[0,-1,0], [0,0,-1], [1,0,0.]])
    R_Cam2Cam = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1.0]])

    points_top_homo_img = np.array(
        [
            [bbox2d[0], bbox2d[1], 1.0],
            [bbox2d[0], bbox2d[3], 1.0],
            [bbox2d[2], bbox2d[3], 1.0],
            [bbox2d[2], bbox2d[1], 1.0],
        ],
        dtype=np.float,
    )

    points_top_homo = points_top_homo_img * float(0.01)
    points_top_homo_cam = np.matmul(np.linalg.inv(RT_cam2image), points_top_homo.T).T
    points_homo = np.matmul(np.linalg.inv(R_Cam2Cam), points_top_homo_cam.T).T
    points_homo = np.hstack((points_homo, np.ones((len(points_homo), 1))))
    points_top_homo_lidar=np.matmul(inverse(RT_lidar2cam),points_homo.T).T[:,0:3]
    points_top_homo_lidar2 = np.matmul(RT_cam2lidar, points_homo.T).T[:, 0:3]

    points = np.vstack([points_top_homo_lidar2, points_top_homo_lidar])

    return points

box =   [565,880,1050,1395]
rt=[0.9999735284469589,0.0027222073873589127,0.006746089562810042,0.0038992750723980227,-0.006782368513432887,0.013787331476714706,0.9998819232858188,1.8052628875768455,0.002628793871735708,-0.9999012511882736,0.013805036302812365,-0.5443215279299205,0,0,0,1]
cameraMatric= [3156.9787100000003,0,1931.26698,0,3156.9787100000003,1081.7780300000002,0,0,1]

box = np.array(box)

rt = np.array(rt)
rt = rt.reshape(4, 4)

cameraMatric = np.array(cameraMatric)
cameraMatric = cameraMatric.reshape(3, 3)

coord = ROI_Frustm(box, rt, cameraMatric)

print(coord)

# coding:utf-8
'''
Created
'''
import numpy as np


def bbox3d_lidar2cam(corners, RT_cam2lidar, Intrinsic_cam):
    assert len(corners.shape) == 2, "points.shape must=(8,3)"
    points_homo = np.hstack((corners, np.ones((len(corners), 1))))
    R = RT_cam2lidar[0:3, 0:3]
    T = RT_cam2lidar[0:3, 3:4]
    RT_lidar2cam = np.zeros((4, 4))
    RT_lidar2cam[0:3, 0:3] = np.linalg.inv(R)
    RT_lidar2cam[0:3, 3:4] = -1*np.matmul(np.linalg.inv(R), T)
    RT_lidar2cam[3, 3] = 1.0

    RT_cam2image = np.array(Intrinsic_cam).reshape(3, 3)
    # R_Cam2Cam=np.array([[0,-1,0], [0,0,-1], [1,0,0.]])
    R_Cam2Cam = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1.]])

    points_top_homo_cam = np.matmul(RT_lidar2cam, points_homo.T).T[:, 0:3]
    points_top_homo_cam = np.matmul(R_Cam2Cam, points_top_homo_cam.T).T
    points_top_homo_img = np.matmul(RT_cam2image, points_top_homo_cam.T).T
    points_top_homo_img = np.divide(
        points_top_homo_img, points_top_homo_cam[:, 2:3])[:, 0:2]

    return points_top_homo_img


def ROI(bbox2d, RT_cam2lidar, Intrinsic_cam, points):
    assert len(points.shape) == 2 and points.shape[1] == 3, "points.shape must=(N,3)"
    assert len(bbox2d.shape) == 1 and bbox2d.shape[0] == 4, "bbox2d.shape must=(4)"
    # points=points[points[:,0]>0,:]  # keep forward points
    points_homo = np.hstack((points, np.ones((len(points), 1))))

    R = RT_cam2lidar[0:3, 0:3]
    T = RT_cam2lidar[0:3, 3:4]
    RT_lidar2cam = np.zeros((4, 4))
    RT_lidar2cam[0:3, 0:3] = np.linalg.inv(R)
    RT_lidar2cam[0:3, 3:4] = -1 * np.matmul(np.linalg.inv(R), T)
    RT_lidar2cam[3, 3] = 1.0

    RT_lidar2cam = np.linalg.inv(RT_cam2lidar)

    RT_cam2image = np.array(Intrinsic_cam).reshape(3, 3)
    # R_Cam2Cam=np.array([[0,-1,0], [0,0,-1], [1,0,0.]])
    R_Cam2Cam = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1.0]])
    points_top_homo_cam = np.matmul(RT_lidar2cam, points_homo.T).T[:, 0:3]
    points_top_homo_cam = np.matmul(R_Cam2Cam, points_top_homo_cam.T).T
    points_top_homo_img = np.matmul(RT_cam2image, points_top_homo_cam.T).T
    points_top_homo_img = np.divide(points_top_homo_img, points_top_homo_cam[:, 2:3])

    l1 = np.logical_and(
        bbox2d[0] <= points_top_homo_img[:, 0], bbox2d[2] >= points_top_homo_img[:, 0]
    )
    l2 = np.logical_and(
        bbox2d[1] <= points_top_homo_img[:, 1], bbox2d[3] >= points_top_homo_img[:, 1]
    )
    keep_index = np.logical_and(l1, l2)
    front_limit = points_top_homo_cam[:, 2] > 0
    keep_index = np.logical_and(keep_index, front_limit)

    return keep_index



rtc2l = [
    -0.9991581301969021,
    0.01019100583537266,
    0.03973803472964759,
    -0.3188947721608751,
    -0.039678965847527066,
    0.006251708040541635,
    -0.9991929546900605,
    -0.7558312776522003,
    -0.010431399499362023,
    -0.9999285264012086,
    -0.005841743276233338,
    -0.7604589975263812,
    0,
    0,
    0,
    1,
]

cameraMatric = [1833.7293701171875, 0, 1936.8907470703125,
                0, 1845.0826416015625, 1111.7017822265625, 0, 0, 1]
corners = [[2, -19, -0.4],
           # corners = [[2.670038938522339,-19.532438278198242,-0.4300000071525574],
           # [2.7500393390655518,-24.142438888549805,-0.4300000071525574],
           # [2.670038938522339,-19.532438278198242,-2.0199999809265137],
           # [2.7500393390655518,-24.142438888549805,-2.0199999809265137],
           # [4.759960651397705,-24.107561111450195,-0.4300000071525574],
           # [4.679960250854492,-19.497560501098633,-0.4300000071525574],
           # [4.759960651397705,-24.107561111450195,-2.0199999809265137],
           # [4.679960250854492,-19.497560501098633,-2.0199999809265137]
           ]

vs = np.array(corners)
rt = np.array(rtc2l)
rt = rt.reshape(4, 4)
cm = np.array(cameraMatric)
cm = cm.reshape(3, 3)
coord = bbox3d_lidar2cam(vs, rt, cm)
print(coord)

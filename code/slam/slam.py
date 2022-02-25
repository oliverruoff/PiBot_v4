import math


class Slam:
    """This class is used for localization and mapping of a robot
       within a two dimensional coordinate system.
    """

    def __init__(self):
        pass

    def _2d_distance(self, point_1, point_2):
        return math.sqrt(math.pow(point_2[0] - point_1[0], 2) + math.pow(point_2[1] - point_1[1], 2))

    def _get_center_point_of_cloud(self, point_cloud):
        avg_x = sum([i[0] for i in point_cloud])/len(point_cloud)
        avg_y = sum([i[1] for i in point_cloud])/len(point_cloud)
        return (avg_x, avg_y)

    def _rotate_point(self, origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in degree.
        """

        angle = math.radians(angle)

        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def score_2d_clouds(self, cloud_1, cloud_2):
        """Calculates the average distance of the points within two 2D point clouds.

        Args:
            cloud_1 (list): List of x,y coordinate iterables
            cloud_2 (list): List of x,y coordinate iterables

        Returns:
            float: Average distance between coordinates in two 2D point clouds.
        """
        distances = []
        for i in range(min([len(cloud_1), len(cloud_2)])):
            distances.append(self._2d_distance(cloud_1[i], cloud_2[i]))
        score = sum(distances)/len(distances)
        print('Score:', score)  # TODO: Remove after debugging
        return score

    def translate_cloud(self, point_cloud, x_offset, y_offset):
        """Translates a list containing 2D points in x and y direction.

        Args:
            point_cloud (list): List of x,y coordinate iterables
            x_offset (float): offset in x direction for which the points will be translated
            y_offset (float): offset in y direction for which the points will be translated

        Returns:
            list: Resulting 2D point list ( [(x0,y0), (x1,y1), ...] )
        """
        return [(i[0]+x_offset, i[1]+y_offset) for i in point_cloud]

    def rotate_cloud(self, point_cloud, angle):
        """Rotates a point cloud around its center point for a given angle in degree.

        Args:
            point_cloud (list): List of x,y coordinate iterables
            angle (float): Angle in degree 

        Returns:
            list: Resulting 2D point list ( [(x0,y0), (x1,y1), ...] )
        """
        origin = self._get_center_point_of_cloud(point_cloud)
        rotated_point_cloud = []
        for point in point_cloud:
            rotated_point_cloud.append(
                (self._rotate_point(origin, point, angle)))
        return rotated_point_cloud

    def find_translation(self, cloud_1, cloud_2, for_x, termination_score):
        last_score = self.score_2d_clouds(cloud_1, cloud_2)
        new_score = 0
        moved_cloud = cloud_2

        step_size = 1
        offset = 0
        mode = 0  # 0 == check in positive direction // 1 == check in negative direction // 2 == stop
        while mode < 2:
            new_offset = offset+step_size if mode == 0 else offset-step_size
            if for_x:
                test_cloud = self.translate_cloud(cloud_2, new_offset, 0)
            else:
                test_cloud = self.translate_cloud(cloud_2, 0, new_offset)
            new_score = self.score_2d_clouds(cloud_1, test_cloud)
            print('New score:', new_score)
            if new_score < last_score:
                last_score = new_score
                offset = new_offset
                moved_cloud = test_cloud
            else:
                mode += 1
        return offset, moved_cloud

    def find_rotation(self, cloud_1, cloud_2, termination_score):
        return 0, cloud_2  # TODO: Implement

    def find_cloud_translation_and_rotation(self, cloud_1, cloud_2, termination_score=5):

        print("Trying to get x_translation")
        x_translation = self.find_translation(
            cloud_1, cloud_2, for_x=True, termination_score=termination_score)
        print("Result:", x_translation[0])
        print("Trying to get y_translation")
        y_translation = self.find_translation(
            cloud_1, x_translation[1], for_x=False, termination_score=termination_score)
        print("Result:", y_translation[0])
        print("Trying to get rotation")
        rotation = self.find_rotation(
            cloud_1, y_translation[1], termination_score)

        return x_translation[0], y_translation[0], rotation[0], rotation[1]

from dataclasses import dataclass
import math

@dataclass(frozen=True)
class GeoPoint:
    lat: float
    lon: float

    def distance_to (self, other: GeoPoint) -> float:
        """
        uses Euclidean distance, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, ensure both points are in the same metric
        (which they should never not be!)

        :param other: geo point to find distance to

        :return: float of the distance between two points
        """
        return math.dist((self.lat, other.lat), (self.lon, other.lon))
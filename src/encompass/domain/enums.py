from enum import Enum

# is used during stage 4, EQUIRECTANGULAR for splitting and searching a pano and PERSPECTIVE for single images
class Projection(Enum):
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    PERSPECTIVE = "PERSPECTIVE"

# used to track if we should be clearing stored panos, is to help stay in line with the street view TOS
class RetentionPolicy(Enum):
    EVICT_EAGER = "EAGER"
    PERSIST_ALLOWED = "PERSIST_ALLOWED"

# used by the pipeline state machine to broadcast the current state to anything listening ui, terminal, ect
class PipelineState(Enum):
    IDLE = "IDLE"
    FILTERING_ATTRIBUTES = "FILTERING_ATTRIBUTES"
    GENERATING_CANDIDATES = "GENERATING_CANDIDATES"
    FETCHING = "FETCHING"
    SLICING = "SLICING"
    SCORING = "SCORING"
    CASCADING = "CASCADING"
    COMPLETE = "COMPLETE"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"

# used to assign the slices of the panos, order here is important the enum is clockwise order, note is that front
# is the front of the image, not north, these positions are not the cardinal directions
class Direction(Enum):
    FRONT = "FRONT"
    FRONT_RIGHT = "FRONT_RIGHT"
    RIGHT = "RIGHT"
    BACK_RIGHT = "BACK_RIGHT"
    BACK = "BACK"
    BACK_LEFT = "BACK_LEFT"
    LEFT = "LEFT"
    FRONT_LEFT = "FRONT_LEFT"

# used for setting road finding rules
class JunctionType(Enum):
    T_JUNCTION = "T_JUNCTION"
    CROSSROADS = "CROSSROADS"
    ROUNDABOUT = "ROUNDABOUT"
    Y_JUNCTION = "Y_JUNCTION"
    FORK = "FORK"
    DEAD_END = "DEAD_END"
    NONE = "NONE"

class RoadClass(Enum):
    RESIDENTIAL = "RESIDENTIAL"
    SERVICE = "SERVICE"
    TERTIARY = "TERTIARY"
    SECONDARY = "SECONDARY"
    PRIMARY = "PRIMARY"
    TRUNK = "TRUNK"
    MOTORWAY = "MOTORWAY"
    FOOTWAY = "FOOTWAY"
    PEDESTRIAN = "PEDESTRIAN"
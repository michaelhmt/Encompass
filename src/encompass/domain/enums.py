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
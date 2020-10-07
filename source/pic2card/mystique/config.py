"""
Gloabal settings and constants.
"""
import os

# max 2mb
IMG_MAX_UPLOAD_SIZE = 2e+6

# tf-serving url
TF_SERVING_URL = os.environ.get("TF_SERVING_URL",
                                "http://172.17.0.5:8501")
TF_SERVING_MODEL_NAME = "mystique"
ENABLE_TF_SERVING = os.environ.get("ENABLE_TF_SERVING",
                                   False)
TF_FROZEN_MODEL_PATH = os.path.join(os.path.dirname(__file__),
                                    "../model/frozen_inference_graph.pb")
TF_LABEL_PATH = os.path.join(os.path.dirname(__file__),
                             "training/object-detection.pbtxt")

# Pytorch model settings.
PTH_MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../model/pth_models/faster-rcnn-2020-05-31-1590943544-epochs_25.pth")

DETR_MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../model/pth_models/detr_trace.pt")


# image hosting max size and default image url
IMG_MAX_HOSTING_SIZE = 1000000
DEFAULT_IMG_HOSTING = "https://lh3.googleusercontent.com/-snm-WznsB3k/XrAWKVCBC3I/AAAAAAAAB8Y/tR-2f8CzboQCmyTzrAfj9Xtvnbeh9PJ8QCK8BGAsYHg/s0/2020-05-04.png" # noqa


# Class labels
ID_TO_LABEL = {
    0: 'background',
    1: "textbox",
    2: "radiobutton",
    3: "checkbox",
    4: "actionset",
    5: "image",
    6: "rating"
}

# Extract properties method plug-ins
# keys are detected object class
# values are the module path for its respective methods
PROPERTY_EXTRACTOR_FUNC = {
    "textbox": "mystique.extract_properties.CollectProperties.textbox",
    "checkbox": "mystique.extract_properties.CollectProperties.checkbox",
    "radiobutton": "mystique.extract_properties.CollectProperties.radiobutton",
    "image": "mystique.extract_properties.CollectProperties.image",
    "actionset": "mystique.extract_properties.CollectProperties.actionset"
}

# Font size and weight property class registry
FONT_SPEC_REGISTRY = {
    "font_morph": "mystique.font_properties.FontPropMorph",
    "font_bbox": "mystique.font_properties.FontPropBoundingBox"
}
# active font prop pipelne
ACTIVE_FONTSPEC_NAME = "font_bbox"

# image detection swtiching paramater
# On True [ uses custom image pipeline for image objects]
# On False [ uses RCNN model image obejcts ]
# Default is False
# USE_CUSTOM_IMAGE_PIPELINE = False

# RCNN model confidence score cutoff
MODEL_CONFIDENCE = 80.0

# Extra textbox padding - 5px
TEXTBOX_PADDING = 5

MODEL_REGISTRY = {
    "tf_faster_rcnn": "mystique.detect_objects.ObjectDetection",
    "tfs_faster_rcnn": "mystique.detect_objects.TfsObjectDetection",
    # "pth_faster_rcnn": "mystique.obj_detect.PtObjectDetection",
    "pth_detr": "mystique.obj_detect.DetrOD",
    "pth_detr_cpp": "mystique.obj_detect.DetrCppOD"
}

ACTIVE_MODEL_NAME = os.environ.get("ACTIVE_MODEL_NAME", "tf_faster_rcnn")

# Noise objects removal IOU threshold
IOU_THRESHOLD = 0.5

# Threshold values of w,h ratio of each image object labels
IMAGE_SIZE_RATIOS = {
        (10.23, 11.92): "Small",
        (19.99, 15.0): "Medium",
        (24.51, 16.33): "Large"
}
# Threshold values of mid point distance between 2 design objects column with
# labels
COLUMN_WIDTH_DISTANCE = {
        (1.0, 46.63): "auto",
        (1.0, 80.40): "stretch"
}
# Threshold values of the mid point distance for the last column in the columns
# and the input image's width, height for the column width labels
LAST_COLUMN_THRESHOLD = {
        (1.0, 3.68): "stretch",
        (1.0, 22.40): "auto"
}
# COLUMNSET GROUPING THRESHOLDS
COLUMNSET_GROUPING = {
        "ymin_difference": 10.0,
        "ymax-ymin_difference": 3,
        "xmax-xmin_difference": 100
}

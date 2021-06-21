# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.6 (default, Dec 16 2020, 17:27:54)
# [GCC 9.3.0]
# Embedded file name: /home/vpraveen/.cache/dazel/_dazel_vpraveen/216c8b41e526c3295d3b802489ac2034/execroot/ai_infra/bazel-out/k8-fastbuild/bin/magnet/packages/iva/build_wheel.runfiles/ai_infra/iva/detectnet_v2/proto/augmentation_config_pb2.py
# Compiled at: 2021-02-05 20:37:47
# Size of source mod 2**32: 19056 bytes
import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name='iva/detectnet_v2/proto/augmentation_config.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=(_b(
        '\n0iva/detectnet_v2/proto/augmentation_config.proto"Ó\n\n\x12AugmentationConfig\x12G\n\rpreprocessing\x18\x01 \x01(\x0b2!.AugmentationConfig.PreprocessingR\rpreprocessing\x12Z\n\x14spatial_augmentation\x18\x02 \x01(\x0b2\'.AugmentationConfig.SpatialAugmentationR\x13spatialAugmentation\x12T\n\x12color_augmentation\x18\x03 \x01(\x0b2%.AugmentationConfig.ColorAugmentationR\x11colorAugmentation\x1aý\x03\n\rPreprocessing\x12,\n\x12output_image_width\x18\x01 \x01(\rR\x10outputImageWidth\x12.\n\x13output_image_height\x18\x02 \x01(\rR\x11outputImageHeight\x12(\n\x10output_image_min\x18\x0e \x01(\rR\x0eoutputImageMin\x12(\n\x10output_image_max\x18\x0f \x01(\rR\x0eoutputImageMax\x120\n\x14output_image_channel\x18\r \x01(\rR\x12outputImageChannel\x12\x1b\n\tcrop_left\x18\x04 \x01(\rR\x08cropLeft\x12\x19\n\x08crop_top\x18\x05 \x01(\rR\x07cropTop\x12\x1d\n\ncrop_right\x18\x06 \x01(\rR\tcropRight\x12\x1f\n\x0bcrop_bottom\x18\x07 \x01(\rR\ncropBottom\x12$\n\x0emin_bbox_width\x18\x08 \x01(\x02R\x0cminBboxWidth\x12&\n\x0fmin_bbox_height\x18\t \x01(\x02R\rminBboxHeight\x12\x1f\n\x0bscale_width\x18\n \x01(\x02R\nscaleWidth\x12!\n\x0cscale_height\x18\x0b \x01(\x02R\x0bscaleHeight\x1aÊ\x02\n\x13SpatialAugmentation\x12+\n\x11hflip_probability\x18\x01 \x01(\x02R\x10hflipProbability\x12+\n\x11vflip_probability\x18\x02 \x01(\x02R\x10vflipProbability\x12\x19\n\x08zoom_min\x18\x03 \x01(\x02R\x07zoomMin\x12\x19\n\x08zoom_max\x18\x04 \x01(\x02R\x07zoomMax\x12&\n\x0ftranslate_max_x\x18\x05 \x01(\x02R\rtranslateMaxX\x12&\n\x0ftranslate_max_y\x18\x06 \x01(\x02R\rtranslateMaxY\x12$\n\x0erotate_rad_max\x18\x07 \x01(\x02R\x0crotateRadMax\x12-\n\x12rotate_probability\x18\x08 \x01(\x02R\x11rotateProbability\x1aô\x01\n\x11ColorAugmentation\x12,\n\x12color_shift_stddev\x18\x01 \x01(\x02R\x10colorShiftStddev\x12(\n\x10hue_rotation_max\x18\x02 \x01(\x02R\x0ehueRotationMax\x120\n\x14saturation_shift_max\x18\x03 \x01(\x02R\x12saturationShiftMax\x12,\n\x12contrast_scale_max\x18\x05 \x01(\x02R\x10contrastScaleMax\x12\'\n\x0fcontrast_center\x18\x08 \x01(\x02R\x0econtrastCenterb\x06proto3'
    )))
_AUGMENTATIONCONFIG_PREPROCESSING = _descriptor.Descriptor(
    name='Preprocessing',
    full_name='AugmentationConfig.Preprocessing',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='output_image_width',
            full_name='AugmentationConfig.Preprocessing.output_image_width',
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='outputImageWidth',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='output_image_height',
            full_name='AugmentationConfig.Preprocessing.output_image_height',
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='outputImageHeight',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='output_image_min',
            full_name='AugmentationConfig.Preprocessing.output_image_min',
            index=2,
            number=14,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='outputImageMin',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='output_image_max',
            full_name='AugmentationConfig.Preprocessing.output_image_max',
            index=3,
            number=15,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='outputImageMax',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='output_image_channel',
            full_name='AugmentationConfig.Preprocessing.output_image_channel',
            index=4,
            number=13,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='outputImageChannel',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='crop_left',
            full_name='AugmentationConfig.Preprocessing.crop_left',
            index=5,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='cropLeft',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='crop_top',
            full_name='AugmentationConfig.Preprocessing.crop_top',
            index=6,
            number=5,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='cropTop',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='crop_right',
            full_name='AugmentationConfig.Preprocessing.crop_right',
            index=7,
            number=6,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='cropRight',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='crop_bottom',
            full_name='AugmentationConfig.Preprocessing.crop_bottom',
            index=8,
            number=7,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='cropBottom',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='min_bbox_width',
            full_name='AugmentationConfig.Preprocessing.min_bbox_width',
            index=9,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='minBboxWidth',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='min_bbox_height',
            full_name='AugmentationConfig.Preprocessing.min_bbox_height',
            index=10,
            number=9,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='minBboxHeight',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='scale_width',
            full_name='AugmentationConfig.Preprocessing.scale_width',
            index=11,
            number=10,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='scaleWidth',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='scale_height',
            full_name='AugmentationConfig.Preprocessing.scale_height',
            index=12,
            number=11,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='scaleHeight',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=327,
    serialized_end=836)
_AUGMENTATIONCONFIG_SPATIALAUGMENTATION = _descriptor.Descriptor(
    name='SpatialAugmentation',
    full_name='AugmentationConfig.SpatialAugmentation',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='hflip_probability',
            full_name='AugmentationConfig.SpatialAugmentation.hflip_probability',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='hflipProbability',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='vflip_probability',
            full_name='AugmentationConfig.SpatialAugmentation.vflip_probability',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='vflipProbability',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='zoom_min',
            full_name='AugmentationConfig.SpatialAugmentation.zoom_min',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='zoomMin',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='zoom_max',
            full_name='AugmentationConfig.SpatialAugmentation.zoom_max',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='zoomMax',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='translate_max_x',
            full_name='AugmentationConfig.SpatialAugmentation.translate_max_x',
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='translateMaxX',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='translate_max_y',
            full_name='AugmentationConfig.SpatialAugmentation.translate_max_y',
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='translateMaxY',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='rotate_rad_max',
            full_name='AugmentationConfig.SpatialAugmentation.rotate_rad_max',
            index=6,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='rotateRadMax',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='rotate_probability',
            full_name=
            'AugmentationConfig.SpatialAugmentation.rotate_probability',
            index=7,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='rotateProbability',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=839,
    serialized_end=1169)
_AUGMENTATIONCONFIG_COLORAUGMENTATION = _descriptor.Descriptor(
    name='ColorAugmentation',
    full_name='AugmentationConfig.ColorAugmentation',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='color_shift_stddev',
            full_name='AugmentationConfig.ColorAugmentation.color_shift_stddev',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='colorShiftStddev',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='hue_rotation_max',
            full_name='AugmentationConfig.ColorAugmentation.hue_rotation_max',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='hueRotationMax',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='saturation_shift_max',
            full_name=
            'AugmentationConfig.ColorAugmentation.saturation_shift_max',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='saturationShiftMax',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='contrast_scale_max',
            full_name='AugmentationConfig.ColorAugmentation.contrast_scale_max',
            index=3,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='contrastScaleMax',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='contrast_center',
            full_name='AugmentationConfig.ColorAugmentation.contrast_center',
            index=4,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=(float(0)),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='contrastCenter',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1172,
    serialized_end=1416)
_AUGMENTATIONCONFIG = _descriptor.Descriptor(
    name='AugmentationConfig',
    full_name='AugmentationConfig',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='preprocessing',
            full_name='AugmentationConfig.preprocessing',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='preprocessing',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='spatial_augmentation',
            full_name='AugmentationConfig.spatial_augmentation',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='spatialAugmentation',
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='color_augmentation',
            full_name='AugmentationConfig.color_augmentation',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name='colorAugmentation',
            file=DESCRIPTOR)
    ],
    extensions=[],
    nested_types=[
        _AUGMENTATIONCONFIG_PREPROCESSING,
        _AUGMENTATIONCONFIG_SPATIALAUGMENTATION,
        _AUGMENTATIONCONFIG_COLORAUGMENTATION
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=53,
    serialized_end=1416)
_AUGMENTATIONCONFIG_PREPROCESSING.containing_type = _AUGMENTATIONCONFIG
_AUGMENTATIONCONFIG_SPATIALAUGMENTATION.containing_type = _AUGMENTATIONCONFIG
_AUGMENTATIONCONFIG_COLORAUGMENTATION.containing_type = _AUGMENTATIONCONFIG
_AUGMENTATIONCONFIG.fields_by_name[
    'preprocessing'].message_type = _AUGMENTATIONCONFIG_PREPROCESSING
_AUGMENTATIONCONFIG.fields_by_name[
    'spatial_augmentation'].message_type = _AUGMENTATIONCONFIG_SPATIALAUGMENTATION
_AUGMENTATIONCONFIG.fields_by_name[
    'color_augmentation'].message_type = _AUGMENTATIONCONFIG_COLORAUGMENTATION
DESCRIPTOR.message_types_by_name['AugmentationConfig'] = _AUGMENTATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
AugmentationConfig = _reflection.GeneratedProtocolMessageType(
    'AugmentationConfig', (_message.Message,),
    dict(
        Preprocessing=(_reflection.GeneratedProtocolMessageType(
            'Preprocessing', (_message.Message,),
            dict(DESCRIPTOR=_AUGMENTATIONCONFIG_PREPROCESSING,
                 __module__='iva.detectnet_v2.proto.augmentation_config_pb2'))),
        SpatialAugmentation=(_reflection.GeneratedProtocolMessageType(
            'SpatialAugmentation', (_message.Message,),
            dict(DESCRIPTOR=_AUGMENTATIONCONFIG_SPATIALAUGMENTATION,
                 __module__='iva.detectnet_v2.proto.augmentation_config_pb2'))),
        ColorAugmentation=(_reflection.GeneratedProtocolMessageType(
            'ColorAugmentation', (_message.Message,),
            dict(DESCRIPTOR=_AUGMENTATIONCONFIG_COLORAUGMENTATION,
                 __module__='iva.detectnet_v2.proto.augmentation_config_pb2'))),
        DESCRIPTOR=_AUGMENTATIONCONFIG,
        __module__='iva.detectnet_v2.proto.augmentation_config_pb2'))
_sym_db.RegisterMessage(AugmentationConfig)
_sym_db.RegisterMessage(AugmentationConfig.Preprocessing)
_sym_db.RegisterMessage(AugmentationConfig.SpatialAugmentation)
_sym_db.RegisterMessage(AugmentationConfig.ColorAugmentation)
# okay decompiling augmentation_config_pb2.pyc

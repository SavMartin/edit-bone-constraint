import bpy

from editboneconstraint.graph import sort_bones_by_constraints
from editboneconstraint.constraints import ConstraintManager


class EvaluateEditBoneConstraintsOperator(bpy.types.Operator):
    bl_idname = "editbone.evaluate_edit_bone_constraints"
    bl_label = "Evaluate Edit Bone Constraints"

    @classmethod
    def poll(cls, context):
        return context.object.type == "ARMATURE" and context.object.mode == 'EDIT'

    def execute(self, context):
        armature = context.object.data
        sorted_bones = sort_bones_by_constraints(armature)
        for bone in sorted_bones:
            manager = ConstraintManager(bone)
            manager.evaluate()

        # force a viewport refresh since some constraints evaluation do not trigger one
        bpy.context.area.tag_redraw()

        return {"FINISHED"}

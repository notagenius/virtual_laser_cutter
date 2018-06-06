import bpy 
import bpy.ops
import bmesh
import mathutils

filepath = "/doc/sample_Box_fill.svg"
texturepath = "/texture/woody.jpg"
thickness = 0.004

bpy.context.scene.render.engine = 'CYCLES'
bpy.ops.import_curve.svg(filepath = filepath)

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='CURVE')
objList = [obj.name for obj in bpy.context.selected_objects]
objList = sorted(objList)

count = 0
obj_count = 0
obj_coordinate = mathutils.Vector((0,0,0))


for mat in bpy.data.materials:
    if mat.name[0:10]=="Laser_Wood":
        count += 1
        
for obj_current in objList:
    obj_count += 1
    obj = bpy.data.objects[obj_current]
    bpy.context.scene.objects.active=obj
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    obj_coordinate = obj_coordinate + obj.location
    

obj_center = obj_coordinate/obj_count

for obj_current in objList:
    string = "Laser_Wood"+ str(count)
    count += 1
    
    obj = bpy.data.objects[obj_current]
    bpy.context.scene.objects.active=obj
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    obj_new_location = (obj.location - obj_center)*10
    bpy.context.scene.objects.active.scale = (10,10,10)
    bpy.context.scene.objects.active.location = obj_new_location
    bpy.ops.object.convert(target='MESH') 
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    bpy.context.object.modifiers["Solidify"].thickness = thickness
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT') 
    bpy.ops.uv.unwrap()
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.material_slot_remove()
    bpy.ops.object.material_slot_add()
    laser_mat = bpy.data.materials.new(string)
    bpy.context.object.active_material = laser_mat
    texture_image = bpy.data.images.load(filepath=texturepath)
    bpy.data.materials[string].use_nodes = True
    bpy.data.materials[string].node_tree.nodes.clear()
    output=bpy.data.materials[string].node_tree.nodes.new(type = 'ShaderNodeOutputMaterial')
    diffuse=bpy.data.materials[string].node_tree.nodes.new(type = 'ShaderNodeBsdfDiffuse')
    tex_image=bpy.data.materials[string].node_tree.nodes.new(type = 'ShaderNodeTexImage')
    bpy.data.materials[string].node_tree.links.new(tex_image.outputs['Color'], diffuse.inputs['Color'])
    tex_image.image=texture_image
    bpy.data.materials[string].node_tree.links.new(diffuse.outputs['BSDF'], output.inputs['Surface'])
    bpy.context.object.active_material = laser_mat

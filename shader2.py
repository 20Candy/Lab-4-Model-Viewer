
vertex_shader = """
#version 440

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 cColor;

out vec3 miColor;
out vec3 miPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;


void main()
{
    gl_Position = projection * view * model * vec4(position.x, position.y, position.z, 1.0);
    miColor = cColor;
}
"""


fragment_shader ="""
#version 440

layout(location = 0) out vec4 fragColor;

in vec3 miColor;
in vec3 miPos;

void main()
{
    fragColor = 1- vec4(miColor.y, 1, 1, 1);
}
"""

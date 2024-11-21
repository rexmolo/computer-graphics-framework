from app import run
from glsprogram import fromSource
from OpenGL.GL import *
import numpy as np

# vertex shader code
vsCode = """
in vec3 position;
uniform float offset;
void main() 
{
    gl_Position = vec4(position.x + offset,position.y, position.z, 1.0);
}
"""

# fragment shader code
fsCode = """
out vec4 fragColor;
void main()
{
    fragColor = vec4(1.0, 1.0, 0.0, 1.0);
}
"""


def render():
    program = fromSource(vsCode, fsCode)
    positionAttribLoacation = glGetAttribLocation(program, "position")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [
        0.0, 0.8, 0.0,
        0.8, -0.8, 0.0,
        -0.8, -0.8, 0.0,
    ]

    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)
    glBufferData(GL_ARRAY_BUFFER, np.array(positions, dtype=np.float32), GL_STATIC_DRAW)

    glVertexAttribPointer(positionAttribLoacation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(positionAttribLoacation)
    glUseProgram(program)

    offsetLocation = glGetUniformLocation(program, "offset")
    glUniform1f(offsetLocation, 0.5)

    glDrawArrays(GL_TRIANGLES, 0, 3)

run("lab 2: TRIANGLE", render)
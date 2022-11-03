/*
Visual Computing 2022/2023
--------------------------
Samuel Silva, Oct. 2022

Fragment shader for flat-shading. The "flat" qualifier tells the shader not to interpolate per-vertex data and use
just the provoking vertex data.

*/
#version 330

flat in vec4 vColor;
out vec4 out_color;

void main()
{

    out_color = vColor;

    return;

}
#version 330

in vec2 fragTexCoord;
in vec4 fragColor;

uniform sampler2D texture0;
uniform vec4 colDiffuse;
uniform vec2 lightPos;
uniform float lightRadius;

out vec4 finalColor;

// Bloom effect variables
const vec2 size = vec2(640, 360);   // Framebuffer size
const float samples = 11.0;         // Pixels per axis; higher = bigger glow, worse performance
const float quality = 1.0;          // Defines size factor: Lower = smaller glow, better quality

void main()
{
    vec4 sum = vec4(0);
    vec2 sizeFactor = vec2(1) / size * quality;

    // Texel color fetching from texture sampler
    vec4 source = texture(texture0, fragTexCoord);

    const int range = 5;  // should be = (samples - 1) / 2;

    for (int x = -range; x <= range; x++)
    {
        for (int y = -range; y <= range; y++)
        {
            sum += texture(texture0, fragTexCoord + vec2(x, y) * sizeFactor);
        }
    }

    // Calculate bloom effect
    vec4 bloomColor = (sum / (samples * samples)) + source;

    // Lighting effect
    float distance = length(fragTexCoord - lightPos);
    float intensity = 1.0 - smoothstep(lightRadius * 0.5, lightRadius, distance);
    vec4 lightingColor = mix(vec4(0.0, 0.0, 0.0, 0.0), vec4(1.0, 1.0, 1.0, 0.5), intensity) * bloomColor;

    // Final color
    finalColor = lightingColor * colDiffuse;
}
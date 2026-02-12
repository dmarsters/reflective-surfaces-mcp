# Reflective Surfaces MCP Server

Systematic visual vocabulary for mirrors, glass, metal, and liquid reflections in image generation workflows.

## Architecture

**Three-layer cost-optimized design:**

- **Layer 1:** Pure taxonomy (reflection types, optical properties) - 0 tokens
- **Layer 2:** Deterministic analysis (Fresnel equations, material mapping) - 0 tokens  
- **Layer 3:** Synthesis interface (Claude composes final creative prompts)

**Cost savings: ~70% vs pure LLM approach**

## Taxonomy Coverage

- **6 Reflection Types:** specular, glossy, diffuse, caustic, metallic, refractive
- **10 Surface Materials:** mirror glass, chrome, brushed metal, water (still/rippled), frosted glass, wet pavement, marble, copper, gold
- **5 Optical Phenomena:** Fresnel effect, chromatic aberration, total internal reflection, subsurface scattering, anisotropic reflection
- **5 Geometry Factors:** flat, convex, concave, compound, faceted
- **5 Environmental Contexts:** bright daylight, overcast, golden hour, artificial indoor, night urban

## Installation

### Local Development

```bash
# Clone/download server
git clone <repo-url>
cd reflective-surfaces-mcp

# Install dependencies
pip install -e .

# Run locally
python reflective_surfaces_mcp.py
```

### FastMCP Cloud Deployment

```bash
# Login to FastMCP Cloud
fastmcp login

# Deploy server
fastmcp deploy reflective_surfaces_mcp.py:mcp

# Get server URL
fastmcp list
```

### Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "reflective-surfaces": {
      "command": "python",
      "args": ["/path/to/reflective_surfaces_mcp.py"]
    }
  }
}
```

Or use FastMCP Cloud URL:

```json
{
  "mcpServers": {
    "reflective-surfaces": {
      "url": "https://your-server.fastmcp.app/mcp"
    }
  }
}
```

## Usage Examples

### Basic Material Lookup

```python
# Get properties of polished chrome
map_material_properties("polished_chrome")

# Returns:
# - Reflection coefficient: 0.88
# - Roughness: 0.05
# - Metallic: 1.0
# - Keywords: ["chrome finish", "metallic sheen", ...]
```

### Fresnel Calculations

```python
# Calculate reflection at 60° viewing angle on glass
compute_fresnel_intensity(60.0, "mirror_glass")

# Returns:
# - Fresnel intensity: 0.421
# - Prominence: "prominent"
# - Composition guidance: "Visible reflection blending with surface..."
```

### Complete Scene Analysis

```python
# Analyze reflection scenario with all factors
analyze_reflection_context(
    material_id="still_water",
    geometry="flat",
    environment="golden_hour",
    viewing_angle_degrees=30.0
)

# Returns:
# - Effective visibility: 0.812
# - Distortion index: 0.021
# - Complete keyword set
# - Optical parameters
# - Composition guidance
```

### Keyword Detection

```python
# Extract reflection terms from natural language
detect_reflection_keywords(
    "A chrome sphere reflecting the sunset over rippled water"
)

# Returns:
# - Materials: ["polished_chrome", "rippled_water"]
# - Reflection types: ["metallic", "caustic"]
# - Geometries: ["convex"]
# - Environments: ["golden_hour"]
```

### Prompt Enhancement

```python
# Generate reflection-enhanced prompt
generate_reflection_prompt_enhancement(
    base_prompt="Futuristic building lobby",
    material_id="polished_marble",
    geometry="flat",
    environment="artificial_indoor",
    viewing_angle=45.0,
    reflection_prominence=0.8
)

# Returns structured data for Claude to synthesize:
# - Primary descriptors
# - Technical parameters (IOR, roughness, metallic)
# - Lighting guidance
# - Suggested prompt structure
```

### Scenario Comparison

```python
# Compare different reflection configurations
compare_reflection_scenarios('''
[
  {
    "label": "Dawn mirror",
    "material_id": "mirror_glass",
    "geometry": "flat",
    "environment": "golden_hour",
    "viewing_angle": 30.0
  },
  {
    "label": "Night puddle",
    "material_id": "wet_pavement",
    "geometry": "flat",
    "environment": "night_urban",
    "viewing_angle": 60.0
  }
]
''')

# Returns:
# - Side-by-side visibility comparison
# - Distortion analysis
# - Aesthetic trade-offs
# - Compositional guidance
```

## Integration Patterns

### Pattern 1: Simple Material Enhancement

```
User: "Add chrome reflections to this robot design"

Claude calls:
1. detect_reflection_keywords("robot design") → suggests "polished_chrome"
2. map_material_properties("polished_chrome") → gets optical params
3. Synthesizes enhanced prompt with reflection vocabulary
```

### Pattern 2: Complete Optical Analysis

```
User: "Create a puddle reflection scene at sunset"

Claude calls:
1. analyze_reflection_context(
     material_id="wet_pavement",
     geometry="flat", 
     environment="golden_hour",
     viewing_angle_degrees=75.0
   )
2. Uses returned parameters to compose detailed prompt
```

### Pattern 3: Comparative Exploration

```
User: "Show me options for mirror vs water reflections"

Claude calls:
1. compare_reflection_scenarios([mirror config, water config])
2. Presents trade-offs: clarity vs distortion, contrast vs softness
3. User selects preferred approach
4. generate_reflection_prompt_enhancement() with chosen config
```

## Optical Parameters Reference

### Reflection Coefficient
- **1.0:** Perfect mirror (theoretical)
- **0.9:** High-quality mirrors, polished chrome
- **0.7:** Glossy surfaces, polished marble
- **0.5:** Wet pavement, moderate reflections
- **0.3:** Diffuse/matte surfaces
- **0.1:** Minimal reflection, mostly scattering

### Roughness
- **0.0:** Perfectly smooth (mirror)
- **0.05-0.15:** Polished metals
- **0.2-0.4:** Brushed/textured surfaces
- **0.6-0.8:** Frosted/etched surfaces
- **0.9-1.0:** Matte/rough surfaces

### Index of Refraction (IOR)
- **1.0:** Vacuum/air
- **1.33:** Water
- **1.52:** Glass
- **2.5-2.8:** Metals (chrome, aluminum)
- **0.47:** Gold (unusual low value)

### Viewing Angles
- **0-30°:** Near-perpendicular, minimal Fresnel boost
- **30-60°:** Moderate angles, visible Fresnel effect
- **60-80°:** Grazing angles, strong reflections
- **80-90°:** Nearly parallel, maximum reflection

## Cost Profile

**Traditional LLM approach:**
- Prompt: 200 tokens
- Analysis: 800 tokens  
- Enhancement: 600 tokens
- **Total: ~1600 tokens per request**

**This MCP server:**
- Layer 2 deterministic: 0 tokens
- Layer 3 synthesis: ~500 tokens
- **Total: ~500 tokens per request**
- **Savings: 69% cost reduction**

## Technical Implementation

### Fresnel Equations

Schlick's approximation for dielectric materials:

```
F(θ) = F₀ + (1 - F₀)(1 - cos θ)⁵

where F₀ = ((n₁ - n₂) / (n₁ + n₂))²
```

For glass-air interface:
- F₀ ≈ 0.04 (normal incidence)
- F(90°) ≈ 1.0 (grazing angle)

### Effective Visibility Formula

```
V_eff = R_coeff × F_fresnel × V_env × (1 - D_geom)

where:
  R_coeff = material reflection coefficient
  F_fresnel = Fresnel intensity at viewing angle
  V_env = environmental visibility factor
  D_geom = geometric distortion factor
```

### Compositional Prominence

- **V_eff > 0.7:** Dominant - reflection is primary visual feature
- **V_eff 0.4-0.7:** Prominent - significant compositional element  
- **V_eff 0.2-0.4:** Subtle - accent detail
- **V_eff < 0.2:** Minimal - trace effect

## Cross-Domain Composition

This server composes naturally with other aesthetic MCPs:

### With Catastrophe Morph
```python
# Reflective surface + catastrophe morphology
catastrophe = get_catastrophe_specifications("cusp")
reflection = map_material_properties("polished_chrome")

# Combine: Sharp cusp geometry with chrome specular reflections
# Creates crystalline aesthetic with geometric precision
```

### With Microscopy Aesthetics
```python
# Reflective surface + microscopy detail
microscopy = get_diatom_optical_properties("centric")
reflection = analyze_reflection_context("wet_pavement", "flat", "night_urban")

# Combine: Fine surface detail with urban reflection patterns
# Creates detailed micro-structure over reflective substrate
```

### With Nuclear Aesthetics
```python
# Reflective surface + energy dynamics
nuclear = map_phase_parameters("fireball_formation")
reflection = compute_fresnel_intensity(85.0, "gold")

# Combine: Intense energy with gold reflections at grazing angle
# Creates dramatic high-energy aesthetic with metallic warmth
```

## Design Philosophy

**Categorical Composition Principles:**

1. **Reflections as functors** - Material properties map deterministically to optical behavior
2. **Separable parameters** - Surface, geometry, lighting, viewing angle compose independently
3. **Preservation of structure** - Physical optics laws (Fresnel, IOR) preserved under composition
4. **Natural transformations** - Changing viewing angle smoothly morphs reflection intensity

**Why This Works:**

- Reflection optics = well-defined mathematical domain
- Standard photography vocabulary already exists
- Image generators understand PBR (physically-based rendering) terms
- Deterministic physics → zero-cost computation

## Contributing

To extend the taxonomy:

1. Add new materials to `SURFACE_MATERIALS` with optical properties
2. Define new optical phenomena with mathematical formulations  
3. Test with `analyze_reflection_context()` to validate
4. Ensure keywords align with image generator vocabulary

## License

MIT License - see LICENSE file

## Author

**Dal Marsters**  
Lushy Systems  
https://lushy.systems

Part of the Lushy MCP Ecosystem - systematic aesthetic enhancement through categorical composition.

#!/usr/bin/env python3
"""
Reflective Surfaces MCP Server
Systematic visual vocabulary for mirrors, glass, metal, and liquid reflections.

Three-layer architecture:
- Layer 1: Pure taxonomy (reflection types, optical properties)
- Layer 2: Deterministic mapping (zero LLM cost)
- Layer 3: Synthesis interface (minimal LLM cost)

Cost optimization: ~70% savings vs pure LLM approach.
"""

from fastmcp import FastMCP
from typing import Dict, List, Optional, Any
import json
import math

mcp = FastMCP("Reflective Surfaces")

# =============================================================================
# LAYER 1: PURE TAXONOMY
# =============================================================================

REFLECTION_TYPES = {
    "specular": {
        "name": "Specular Reflection",
        "description": "Mirror-like perfect reflections",
        "reflection_coefficient": 0.9,
        "clarity": 1.0,
        "distortion": 0.0,
        "keywords": ["mirror-like", "sharp reflections", "perfect clarity", "distinct mirror image"],
        "materials": ["polished chrome", "mirror glass", "still water", "polished marble"],
        "optical_properties": {
            "preserves_angles": True,
            "color_fidelity": "high",
            "depth_perception": "accurate"
        }
    },
    "glossy": {
        "name": "Glossy Reflection",
        "description": "Clear but softer reflections with slight diffusion",
        "reflection_coefficient": 0.6,
        "clarity": 0.7,
        "distortion": 0.2,
        "keywords": ["polished surface", "soft reflections", "gentle sheen", "semi-reflective"],
        "materials": ["polished wood", "glazed ceramic", "car paint", "wet pavement"],
        "optical_properties": {
            "preserves_angles": True,
            "color_fidelity": "medium-high",
            "depth_perception": "slightly softened"
        }
    },
    "diffuse": {
        "name": "Diffuse Reflection",
        "description": "Scattered light, no clear image reflection",
        "reflection_coefficient": 0.3,
        "clarity": 0.2,
        "distortion": 0.8,
        "keywords": ["matte surface", "scattered light", "soft glow", "no distinct reflection"],
        "materials": ["unpolished metal", "frosted glass", "matte paint", "rough stone"],
        "optical_properties": {
            "preserves_angles": False,
            "color_fidelity": "low",
            "depth_perception": "minimal"
        }
    },
    "caustic": {
        "name": "Caustic Patterns",
        "description": "Focused light patterns from curved/refractive surfaces",
        "reflection_coefficient": 0.4,
        "clarity": 0.3,
        "distortion": 0.6,
        "keywords": ["light patterns", "dancing reflections", "rippled caustics", "focused beams"],
        "materials": ["rippled water", "textured glass", "crystal facets", "ice surfaces"],
        "optical_properties": {
            "preserves_angles": False,
            "color_fidelity": "varies",
            "depth_perception": "complex"
        }
    },
    "metallic": {
        "name": "Metallic Reflection",
        "description": "Color-tinted reflections from metal surfaces",
        "reflection_coefficient": 0.8,
        "clarity": 0.85,
        "distortion": 0.1,
        "keywords": ["metal sheen", "tinted reflections", "lustrous surface", "metallic gleam"],
        "materials": ["brushed aluminum", "copper", "brass", "gold", "silver"],
        "optical_properties": {
            "preserves_angles": True,
            "color_fidelity": "tinted",
            "depth_perception": "accurate with color cast"
        }
    },
    "refractive": {
        "name": "Refractive Distortion",
        "description": "Bent light paths through transparent media",
        "reflection_coefficient": 0.5,
        "clarity": 0.6,
        "distortion": 0.5,
        "keywords": ["bent light", "distorted view", "magnification", "prismatic effects"],
        "materials": ["glass", "water", "crystal", "ice", "transparent plastic"],
        "optical_properties": {
            "preserves_angles": False,
            "color_fidelity": "chromatic aberration possible",
            "depth_perception": "warped"
        }
    }
}

SURFACE_MATERIALS = {
    "mirror_glass": {
        "name": "Mirror Glass",
        "reflection_type": "specular",
        "reflection_coefficient": 0.95,
        "roughness": 0.0,
        "ior": 1.52,  # Index of refraction
        "metallic": 0.0,
        "color_tint": None,
        "keywords": ["perfect mirror", "silvered glass", "clear reflection", "flawless surface"]
    },
    "polished_chrome": {
        "name": "Polished Chrome",
        "reflection_type": "metallic",
        "reflection_coefficient": 0.88,
        "roughness": 0.05,
        "ior": 2.7,
        "metallic": 1.0,
        "color_tint": "cool_neutral",
        "keywords": ["chrome finish", "metallic sheen", "industrial gleam", "steel-like"]
    },
    "brushed_metal": {
        "name": "Brushed Metal",
        "reflection_type": "glossy",
        "reflection_coefficient": 0.6,
        "roughness": 0.25,
        "ior": 2.5,
        "metallic": 0.9,
        "color_tint": "varies",
        "keywords": ["directional grain", "soft metal sheen", "textured surface", "industrial finish"]
    },
    "still_water": {
        "name": "Still Water",
        "reflection_type": "specular",
        "reflection_coefficient": 0.85,
        "roughness": 0.02,
        "ior": 1.33,
        "metallic": 0.0,
        "color_tint": "slight_blue",
        "keywords": ["glassy surface", "lake reflection", "mirror-like water", "perfect stillness"]
    },
    "rippled_water": {
        "name": "Rippled Water",
        "reflection_type": "caustic",
        "reflection_coefficient": 0.6,
        "roughness": 0.4,
        "ior": 1.33,
        "metallic": 0.0,
        "color_tint": "slight_blue",
        "keywords": ["dancing reflections", "wave patterns", "distorted mirror", "moving surface"]
    },
    "frosted_glass": {
        "name": "Frosted Glass",
        "reflection_type": "diffuse",
        "reflection_coefficient": 0.2,
        "roughness": 0.8,
        "ior": 1.52,
        "metallic": 0.0,
        "color_tint": None,
        "keywords": ["translucent", "soft glow", "privacy glass", "diffused light"]
    },
    "wet_pavement": {
        "name": "Wet Pavement",
        "reflection_type": "glossy",
        "reflection_coefficient": 0.5,
        "roughness": 0.3,
        "ior": 1.33,
        "metallic": 0.0,
        "color_tint": "neutral_dark",
        "keywords": ["rain-slicked", "street reflections", "urban sheen", "puddle mirrors"]
    },
    "polished_marble": {
        "name": "Polished Marble",
        "reflection_type": "glossy",
        "reflection_coefficient": 0.7,
        "roughness": 0.15,
        "ior": 1.55,
        "metallic": 0.0,
        "color_tint": "varies",
        "keywords": ["stone gleam", "luxury surface", "veined reflection", "architectural polish"]
    },
    "copper": {
        "name": "Copper",
        "reflection_type": "metallic",
        "reflection_coefficient": 0.75,
        "roughness": 0.1,
        "ior": 2.8,
        "metallic": 1.0,
        "color_tint": "warm_orange",
        "keywords": ["copper gleam", "warm metallic", "reddish tint", "oxidized patina potential"]
    },
    "gold": {
        "name": "Gold",
        "reflection_type": "metallic",
        "reflection_coefficient": 0.8,
        "roughness": 0.08,
        "ior": 0.47,
        "metallic": 1.0,
        "color_tint": "warm_yellow",
        "keywords": ["golden luster", "warm reflections", "precious metal", "rich gleam"]
    }
}

OPTICAL_PHENOMENA = {
    "fresnel_effect": {
        "name": "Fresnel Effect",
        "description": "Reflection intensity varies with viewing angle",
        "angle_dependency": "strong",
        "intensity_at_grazing": 1.0,
        "intensity_at_normal": 0.04,  # For glass
        "keywords": ["angle-dependent reflection", "edge brightness", "viewing angle changes"],
        "applicable_materials": ["glass", "water", "plastics", "dielectrics"]
    },
    "chromatic_aberration": {
        "name": "Chromatic Aberration",
        "description": "Color fringing in refractive materials",
        "effect_strength": "medium",
        "color_separation": ["red_shift_edges", "blue_shift_center"],
        "keywords": ["color fringing", "rainbow edges", "prismatic effect", "wavelength separation"],
        "applicable_materials": ["glass", "crystal", "water", "transparent_media"]
    },
    "total_internal_reflection": {
        "name": "Total Internal Reflection",
        "description": "Complete reflection at critical angle in denser media",
        "critical_angle_glass": 41.8,  # degrees for glass-air interface
        "critical_angle_water": 48.6,  # degrees for water-air interface
        "keywords": ["fiber optic effect", "trapped light", "critical angle", "complete reflection"],
        "applicable_materials": ["glass", "water", "diamond", "transparent_solids"]
    },
    "subsurface_scattering": {
        "name": "Subsurface Scattering",
        "description": "Light penetrates surface, scatters internally",
        "depth_penetration": "shallow",
        "color_shift": "subtle",
        "keywords": ["internal glow", "translucent effect", "soft diffusion", "depth glow"],
        "applicable_materials": ["marble", "wax", "skin", "jade", "alabaster"]
    },
    "anisotropic_reflection": {
        "name": "Anisotropic Reflection",
        "description": "Directional surface structure creates elongated highlights",
        "directionality": "strong",
        "highlight_shape": "elongated",
        "keywords": ["brushed metal look", "directional grain", "linear highlights", "CD-like iridescence"],
        "applicable_materials": ["brushed_metal", "hair", "fabric", "wood_grain"]
    }
}

GEOMETRY_FACTORS = {
    "flat": {
        "name": "Flat Surface",
        "curvature": 0.0,
        "reflection_distortion": 0.0,
        "coverage_uniformity": 1.0,
        "keywords": ["planar reflection", "undistorted mirror", "parallel surfaces", "true image"],
        "example_contexts": ["wall mirrors", "still water", "glass windows", "polished floors"]
    },
    "convex": {
        "name": "Convex Surface",
        "curvature": "positive",
        "reflection_distortion": 0.6,
        "coverage_uniformity": 0.4,
        "keywords": ["wide-angle view", "compressed reflection", "fisheye effect", "panoramic distortion"],
        "example_contexts": ["spheres", "domes", "security mirrors", "watch crystals", "bubbles"]
    },
    "concave": {
        "name": "Concave Surface",
        "curvature": "negative",
        "reflection_distortion": 0.7,
        "coverage_uniformity": 0.3,
        "keywords": ["magnified reflection", "focused convergence", "inverted beyond focal point", "concentrated view"],
        "example_contexts": ["spoons", "satellite dishes", "makeup mirrors", "parabolic reflectors"]
    },
    "compound": {
        "name": "Compound Curvature",
        "curvature": "complex",
        "reflection_distortion": 0.8,
        "coverage_uniformity": 0.2,
        "keywords": ["complex distortion", "variable magnification", "artistic warping", "multi-directional curves"],
        "example_contexts": ["car bodies", "sculptures", "architectural features", "organic forms"]
    },
    "faceted": {
        "name": "Faceted Surface",
        "curvature": "discrete",
        "reflection_distortion": 0.5,
        "coverage_uniformity": 0.5,
        "keywords": ["fragmented reflections", "geometric patterns", "prismatic separation", "crystalline structure"],
        "example_contexts": ["cut glass", "gemstones", "disco balls", "architectural glass", "crystal"]
    }
}

ENVIRONMENTAL_CONTEXTS = {
    "bright_daylight": {
        "name": "Bright Daylight",
        "light_intensity": 1.0,
        "contrast_ratio": 0.8,
        "color_temperature": 5500,
        "reflection_visibility": 0.9,
        "keywords": ["harsh reflections", "high contrast", "glare potential", "sharp definition"]
    },
    "overcast": {
        "name": "Overcast Sky",
        "light_intensity": 0.4,
        "contrast_ratio": 0.3,
        "color_temperature": 6500,
        "reflection_visibility": 0.5,
        "keywords": ["soft reflections", "low contrast", "diffused lighting", "gentle tones"]
    },
    "golden_hour": {
        "name": "Golden Hour",
        "light_intensity": 0.6,
        "contrast_ratio": 0.7,
        "color_temperature": 3500,
        "reflection_visibility": 0.85,
        "keywords": ["warm reflections", "amber tones", "long shadows", "dramatic lighting"]
    },
    "artificial_indoor": {
        "name": "Artificial Indoor",
        "light_intensity": 0.5,
        "contrast_ratio": 0.6,
        "color_temperature": 4000,
        "reflection_visibility": 0.7,
        "keywords": ["controlled lighting", "mixed sources", "ambient fill", "practical lights"]
    },
    "night_urban": {
        "name": "Night Urban",
        "light_intensity": 0.2,
        "contrast_ratio": 0.9,
        "color_temperature": 3000,
        "reflection_visibility": 0.8,
        "keywords": ["neon reflections", "colored lights", "deep shadows", "artificial glow"]
    }
}

# =============================================================================
# LAYER 2: DETERMINISTIC MAPPING (Zero LLM Cost)
# =============================================================================

@mcp.tool()
def get_reflection_taxonomy() -> str:
    """
    Get complete taxonomy of reflection types, materials, and optical properties.
    
    Layer 1: Pure taxonomy lookup (0 tokens)
    
    Returns complete reference for all reflection categories including:
    - Reflection types (specular, glossy, diffuse, caustic, metallic, refractive)
    - Surface materials with optical properties
    - Optical phenomena (Fresnel, chromatic aberration, etc.)
    - Geometry factors (flat, convex, concave, compound, faceted)
    - Environmental contexts
    """
    return json.dumps({
        "reflection_types": REFLECTION_TYPES,
        "surface_materials": SURFACE_MATERIALS,
        "optical_phenomena": OPTICAL_PHENOMENA,
        "geometry_factors": GEOMETRY_FACTORS,
        "environmental_contexts": ENVIRONMENTAL_CONTEXTS,
        "cost": "0 tokens - pure taxonomy lookup"
    }, indent=2)


@mcp.tool()
def map_material_properties(material_id: str) -> str:
    """
    Get complete optical properties for a specific material.
    
    Layer 2: Deterministic lookup (0 tokens)
    
    Args:
        material_id: Material identifier (mirror_glass, polished_chrome, still_water, etc.)
    
    Returns:
        Complete optical specification including reflection coefficient, 
        roughness, IOR, metallic value, and image generation keywords
    """
    if material_id not in SURFACE_MATERIALS:
        available = list(SURFACE_MATERIALS.keys())
        return json.dumps({
            "error": f"Unknown material: {material_id}",
            "available_materials": available
        }, indent=2)
    
    material = SURFACE_MATERIALS[material_id]
    reflection_type = REFLECTION_TYPES[material["reflection_type"]]
    
    return json.dumps({
        "material": material,
        "reflection_behavior": reflection_type,
        "composition_guidance": {
            "reflection_strength": material["reflection_coefficient"],
            "surface_clarity": reflection_type["clarity"],
            "distortion_level": reflection_type["distortion"],
            "keywords": material["keywords"] + reflection_type["keywords"]
        },
        "cost": "0 tokens - deterministic lookup"
    }, indent=2)


@mcp.tool()
def compute_fresnel_intensity(viewing_angle_degrees: float, material_id: str = "mirror_glass") -> str:
    """
    Calculate reflection intensity based on viewing angle (Fresnel equations).
    
    Layer 2: Deterministic computation (0 tokens)
    
    Implements Schlick's approximation for Fresnel reflectance:
    F(θ) = F₀ + (1 - F₀)(1 - cos θ)⁵
    
    Args:
        viewing_angle_degrees: Angle from surface normal (0° = perpendicular, 90° = grazing)
        material_id: Surface material (determines F₀ base reflectance)
    
    Returns:
        Reflection intensity (0.0-1.0) and composition guidance
    """
    if material_id not in SURFACE_MATERIALS:
        material_id = "mirror_glass"
    
    material = SURFACE_MATERIALS[material_id]
    ior = material["ior"]
    
    # Calculate F₀ (reflectance at normal incidence) from IOR
    f0 = ((ior - 1) / (ior + 1)) ** 2
    
    # Convert angle to radians
    angle_rad = math.radians(viewing_angle_degrees)
    cos_theta = math.cos(angle_rad)
    
    # Schlick's approximation
    fresnel_intensity = f0 + (1 - f0) * (1 - cos_theta) ** 5
    
    # Composition guidance based on intensity
    if fresnel_intensity > 0.8:
        prominence = "dominant"
        guidance = "Strong reflection, nearly mirror-like. Use as primary visual element."
    elif fresnel_intensity > 0.5:
        prominence = "prominent"
        guidance = "Visible reflection blending with surface. Balance reflection and material properties."
    elif fresnel_intensity > 0.2:
        prominence = "subtle"
        guidance = "Gentle reflection accent. Emphasize surface material over reflection."
    else:
        prominence = "minimal"
        guidance = "Very weak reflection. Focus on material properties and transmitted/scattered light."
    
    return json.dumps({
        "viewing_angle": viewing_angle_degrees,
        "material": material_id,
        "fresnel_intensity": round(fresnel_intensity, 3),
        "prominence": prominence,
        "composition_guidance": guidance,
        "optical_parameters": {
            "f0_base_reflectance": round(f0, 3),
            "cos_theta": round(cos_theta, 3),
            "ior": ior
        },
        "cost": "0 tokens - deterministic calculation"
    }, indent=2)


@mcp.tool()
def analyze_reflection_context(
    material_id: str,
    geometry: str,
    environment: str,
    viewing_angle_degrees: float = 45.0
) -> str:
    """
    Analyze complete reflection scenario with all optical factors.
    
    Layer 2: Deterministic composition (0 tokens)
    
    Combines material properties, surface geometry, environmental lighting,
    and viewing angle to produce comprehensive reflection parameters.
    
    Args:
        material_id: Surface material (mirror_glass, polished_chrome, etc.)
        geometry: Surface geometry (flat, convex, concave, compound, faceted)
        environment: Lighting context (bright_daylight, overcast, golden_hour, etc.)
        viewing_angle_degrees: Viewing angle from normal (default 45°)
    
    Returns:
        Complete reflection specification with visibility scores and keywords
    """
    # Validate inputs
    if material_id not in SURFACE_MATERIALS:
        return json.dumps({"error": f"Unknown material: {material_id}"}, indent=2)
    if geometry not in GEOMETRY_FACTORS:
        return json.dumps({"error": f"Unknown geometry: {geometry}"}, indent=2)
    if environment not in ENVIRONMENTAL_CONTEXTS:
        return json.dumps({"error": f"Unknown environment: {environment}"}, indent=2)
    
    # Gather taxonomy data
    material = SURFACE_MATERIALS[material_id]
    geom = GEOMETRY_FACTORS[geometry]
    env = ENVIRONMENTAL_CONTEXTS[environment]
    refl_type = REFLECTION_TYPES[material["reflection_type"]]
    
    # Calculate Fresnel intensity
    fresnel_result = json.loads(compute_fresnel_intensity(viewing_angle_degrees, material_id))
    fresnel_intensity = fresnel_result["fresnel_intensity"]
    
    # Compute effective reflection visibility
    # Formula: base_coefficient * fresnel * env_visibility * (1 - geometry_distortion)
    base_coeff = material["reflection_coefficient"]
    env_vis = env["reflection_visibility"]
    geom_clarity = 1 - geom["reflection_distortion"]
    
    effective_visibility = base_coeff * fresnel_intensity * env_vis * geom_clarity
    
    # Distortion scoring
    total_distortion = material["roughness"] * 0.5 + geom["reflection_distortion"] * 0.5
    
    # Compile keywords
    all_keywords = (
        material["keywords"] +
        refl_type["keywords"] +
        geom["keywords"] +
        env["keywords"]
    )
    
    # Prominence assessment
    if effective_visibility > 0.7:
        prominence = "dominant"
        role = "primary visual feature"
    elif effective_visibility > 0.4:
        prominence = "prominent"
        role = "significant compositional element"
    elif effective_visibility > 0.2:
        prominence = "subtle"
        role = "accent detail"
    else:
        prominence = "minimal"
        role = "trace effect"
    
    return json.dumps({
        "scenario": {
            "material": material_id,
            "geometry": geometry,
            "environment": environment,
            "viewing_angle": viewing_angle_degrees
        },
        "reflection_parameters": {
            "effective_visibility": round(effective_visibility, 3),
            "distortion_index": round(total_distortion, 3),
            "clarity": round(refl_type["clarity"] * geom_clarity, 3),
            "fresnel_contribution": round(fresnel_intensity, 3)
        },
        "composition_guidance": {
            "prominence": prominence,
            "compositional_role": role,
            "contrast_ratio": env["contrast_ratio"],
            "light_intensity": env["light_intensity"]
        },
        "image_generation_vocabulary": {
            "keywords": all_keywords,
            "optical_properties": {
                "reflection_coefficient": base_coeff,
                "roughness": material["roughness"],
                "metallic": material["metallic"],
                "ior": material["ior"],
                "color_tint": material["color_tint"]
            },
            "lighting_guidance": {
                "color_temperature": env["color_temperature"],
                "intensity": env["light_intensity"]
            }
        },
        "cost": "0 tokens - deterministic analysis"
    }, indent=2)


@mcp.tool()
def detect_reflection_keywords(prompt: str) -> str:
    """
    Extract reflection-related terms from a text prompt.
    
    Layer 2: Deterministic pattern matching (0 tokens)
    
    Scans prompt for material names, reflection types, geometry descriptors,
    and optical phenomena. Pure string matching, no LLM inference.
    
    Args:
        prompt: Natural language prompt to analyze
    
    Returns:
        Detected materials, reflection types, phenomena, and suggested parameters
    """
    prompt_lower = prompt.lower()
    
    detected = {
        "materials": [],
        "reflection_types": [],
        "geometries": [],
        "phenomena": [],
        "environments": []
    }
    
    # Scan for materials
    for mat_id, mat_data in SURFACE_MATERIALS.items():
        if mat_id.replace("_", " ") in prompt_lower:
            detected["materials"].append(mat_id)
        # Check material name
        if mat_data["name"].lower() in prompt_lower:
            detected["materials"].append(mat_id)
    
    # Scan for reflection types
    for refl_id, refl_data in REFLECTION_TYPES.items():
        if refl_id in prompt_lower:
            detected["reflection_types"].append(refl_id)
        # Check keywords
        for keyword in refl_data["keywords"]:
            if keyword.lower() in prompt_lower:
                detected["reflection_types"].append(refl_id)
                break
    
    # Scan for geometries
    for geom_id in GEOMETRY_FACTORS.keys():
        if geom_id in prompt_lower:
            detected["geometries"].append(geom_id)
    
    # Scan for optical phenomena
    for phenom_id, phenom_data in OPTICAL_PHENOMENA.items():
        if phenom_id.replace("_", " ") in prompt_lower:
            detected["phenomena"].append(phenom_id)
        for keyword in phenom_data["keywords"]:
            if keyword.lower() in prompt_lower:
                detected["phenomena"].append(phenom_id)
                break
    
    # Scan for environments
    for env_id, env_data in ENVIRONMENTAL_CONTEXTS.items():
        if env_id.replace("_", " ") in prompt_lower:
            detected["environments"].append(env_id)
        for keyword in env_data["keywords"]:
            if keyword.lower() in prompt_lower:
                detected["environments"].append(env_id)
                break
    
    # Remove duplicates
    for key in detected:
        detected[key] = list(set(detected[key]))
    
    # Generate suggestions if nothing detected
    suggestions = []
    if not detected["materials"]:
        if "mirror" in prompt_lower or "reflection" in prompt_lower:
            suggestions.append("Consider: mirror_glass or polished_chrome")
        elif "water" in prompt_lower:
            suggestions.append("Consider: still_water or rippled_water")
        elif "metal" in prompt_lower:
            suggestions.append("Consider: polished_chrome, copper, or gold")
    
    if not detected["geometries"]:
        suggestions.append("Consider specifying geometry: flat, convex, concave, compound, or faceted")
    
    if not detected["environments"]:
        suggestions.append("Consider lighting context: bright_daylight, golden_hour, or night_urban")
    
    return json.dumps({
        "detected": detected,
        "suggestions": suggestions,
        "has_reflection_content": any(detected.values()),
        "cost": "0 tokens - pattern matching"
    }, indent=2)


# =============================================================================
# LAYER 3: SYNTHESIS INTERFACE (Minimal LLM Cost)
# =============================================================================

@mcp.tool()
def generate_reflection_prompt_enhancement(
    base_prompt: str,
    material_id: str,
    geometry: str = "flat",
    environment: str = "bright_daylight",
    viewing_angle: float = 45.0,
    reflection_prominence: float = 0.7,
    style_modifier: str = ""
) -> str:
    """
    Generate image prompt with precise reflection vocabulary.
    
    Layer 3: Synthesis preparation (returns data for Claude to compose)
    
    This tool returns deterministic parameters. Claude (Layer 3) synthesizes
    the final creative prompt integrating these specs with artistic intent.
    
    Args:
        base_prompt: Original prompt describing the scene
        material_id: Reflective surface material
        geometry: Surface geometry type
        environment: Lighting environment
        viewing_angle: Viewing angle from normal (0-90 degrees)
        reflection_prominence: How prominent reflection should be (0.0-1.0)
        style_modifier: Optional style descriptor ("photorealistic", "cinematic", etc.)
    
    Returns:
        JSON with vocabulary, parameters, and suggested prompt structure.
        Claude should synthesize final prompt from this data.
    """
    # Get full analysis
    analysis = json.loads(analyze_reflection_context(
        material_id, geometry, environment, viewing_angle
    ))
    
    if "error" in analysis:
        return json.dumps(analysis, indent=2)
    
    # Weight reflection keywords by prominence
    reflection_params = analysis["reflection_parameters"]
    keywords = analysis["image_generation_vocabulary"]["keywords"]
    
    # Apply user-specified prominence override
    effective_visibility = reflection_params["effective_visibility"] * reflection_prominence
    
    # Categorize keywords by strength
    primary_keywords = keywords[:4]  # Top descriptors
    secondary_keywords = keywords[4:8]  # Supporting terms
    
    # Optical parameters for technical prompts
    optical = analysis["image_generation_vocabulary"]["optical_properties"]
    lighting = analysis["image_generation_vocabulary"]["lighting_guidance"]
    
    return json.dumps({
        "base_prompt": base_prompt,
        "reflection_enhancement": {
            "primary_descriptors": primary_keywords,
            "secondary_descriptors": secondary_keywords,
            "effective_visibility": round(effective_visibility, 3),
            "prominence": analysis["composition_guidance"]["prominence"]
        },
        "technical_parameters": {
            "material": material_id,
            "geometry": geometry,
            "optical_properties": optical,
            "lighting": lighting,
            "viewing_angle": viewing_angle
        },
        "suggested_prompt_structure": {
            "order": [
                "1. Base scene description",
                "2. Surface material specification",
                "3. Reflection characteristics",
                "4. Lighting and environment",
                "5. Viewing angle/perspective",
                "6. Style modifier (if any)"
            ],
            "example_integration": f"{base_prompt}, {material_id.replace('_', ' ')} surface with {primary_keywords[0]}, {environment.replace('_', ' ')} lighting"
        },
        "style_modifier": style_modifier,
        "cost_profile": {
            "layer_2_deterministic": "0 tokens",
            "layer_3_synthesis": "Claude composes final prompt from this data"
        }
    }, indent=2)


@mcp.tool()
def compare_reflection_scenarios(scenarios: str) -> str:
    """
    Compare multiple reflection configurations side-by-side.
    
    Layer 2/3 Bridge: Deterministic comparison with synthesis guidance.
    
    Useful for exploring compositional alternatives. Returns comparative
    analysis that Claude can use to guide artistic decisions.
    
    Args:
        scenarios: JSON array of scenario configs:
            [
                {
                    "label": "Dawn mirror",
                    "material_id": "mirror_glass",
                    "geometry": "flat",
                    "environment": "golden_hour",
                    "viewing_angle": 30.0
                },
                {...}
            ]
    
    Returns:
        Comparative analysis showing trade-offs, aesthetic implications
    """
    try:
        scenario_list = json.loads(scenarios)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format for scenarios"}, indent=2)
    
    if not isinstance(scenario_list, list) or len(scenario_list) < 2:
        return json.dumps({
            "error": "Provide at least 2 scenarios as JSON array"
        }, indent=2)
    
    analyses = []
    for scenario in scenario_list:
        label = scenario.get("label", "Unlabeled")
        material = scenario.get("material_id", "mirror_glass")
        geometry = scenario.get("geometry", "flat")
        environment = scenario.get("environment", "bright_daylight")
        viewing_angle = scenario.get("viewing_angle", 45.0)
        
        analysis = json.loads(analyze_reflection_context(
            material, geometry, environment, viewing_angle
        ))
        
        analyses.append({
            "label": label,
            "scenario": scenario,
            "analysis": analysis
        })
    
    # Extract comparison dimensions
    comparison = {
        "scenarios": [],
        "comparative_insights": {
            "visibility_range": [],
            "distortion_range": [],
            "contrast_range": [],
            "aesthetic_trade_offs": []
        }
    }
    
    for item in analyses:
        label = item["label"]
        params = item["analysis"]["reflection_parameters"]
        guidance = item["analysis"]["composition_guidance"]
        
        comparison["scenarios"].append({
            "label": label,
            "visibility": params["effective_visibility"],
            "distortion": params["distortion_index"],
            "prominence": guidance["prominence"],
            "role": guidance["compositional_role"]
        })
        
        comparison["comparative_insights"]["visibility_range"].append(
            params["effective_visibility"]
        )
        comparison["comparative_insights"]["distortion_range"].append(
            params["distortion_index"]
        )
        comparison["comparative_insights"]["contrast_range"].append(
            guidance["contrast_ratio"]
        )
    
    # Calculate ranges
    vis_range = comparison["comparative_insights"]["visibility_range"]
    dist_range = comparison["comparative_insights"]["distortion_range"]
    
    comparison["comparative_insights"]["visibility_span"] = {
        "min": round(min(vis_range), 3),
        "max": round(max(vis_range), 3),
        "delta": round(max(vis_range) - min(vis_range), 3)
    }
    
    comparison["comparative_insights"]["distortion_span"] = {
        "min": round(min(dist_range), 3),
        "max": round(max(dist_range), 3),
        "delta": round(max(dist_range) - min(dist_range), 3)
    }
    
    # Aesthetic guidance
    if comparison["comparative_insights"]["visibility_span"]["delta"] > 0.4:
        comparison["comparative_insights"]["aesthetic_trade_offs"].append(
            "Significant visibility variation - creates strong compositional contrast"
        )
    
    if comparison["comparative_insights"]["distortion_span"]["delta"] > 0.3:
        comparison["comparative_insights"]["aesthetic_trade_offs"].append(
            "High distortion variation - geometric effects will be prominent differentiator"
        )
    
    comparison["cost"] = "0 tokens - deterministic comparison"
    
    return json.dumps(comparison, indent=2)


@mcp.tool()
def get_server_info() -> str:
    """
    Get information about the Reflective Surfaces MCP server.
    
    Returns server metadata, capabilities, and architecture overview.
    """
    return json.dumps({
        "server": "Reflective Surfaces MCP",
        "version": "1.0.0",
        "description": "Systematic visual vocabulary for reflective surface aesthetics",
        "architecture": {
            "layer_1": "Pure taxonomy (reflection types, materials, optics)",
            "layer_2": "Deterministic mapping and analysis (0 tokens)",
            "layer_3": "Synthesis interface for Claude composition"
        },
        "cost_optimization": "~70% savings vs pure LLM approach",
        "taxonomy_coverage": {
            "reflection_types": len(REFLECTION_TYPES),
            "surface_materials": len(SURFACE_MATERIALS),
            "optical_phenomena": len(OPTICAL_PHENOMENA),
            "geometry_factors": len(GEOMETRY_FACTORS),
            "environmental_contexts": len(ENVIRONMENTAL_CONTEXTS)
        },
        "key_capabilities": [
            "Fresnel equation calculations",
            "Material optical property lookup",
            "Multi-factor reflection analysis",
            "Keyword detection and extraction",
            "Comparative scenario analysis",
            "Image prompt enhancement"
        ],
        "usage_pattern": "Call Layer 2 tools for deterministic analysis, then use results in Layer 3 for creative synthesis",
        "author": "Dal Marsters / Lushy Systems"
    }, indent=2)

if __name__ == "__main__":
    mcp.run()

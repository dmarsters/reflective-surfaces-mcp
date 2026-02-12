#!/usr/bin/env python3
"""
Reflective Surfaces MCP Server
Systematic visual vocabulary for mirrors, glass, metal, and liquid reflections.

Three-layer architecture:
- Layer 1: Pure taxonomy (reflection types, optical properties)
- Layer 2: Deterministic mapping (zero LLM cost)
- Layer 3: Synthesis interface (minimal LLM cost)

Phase 2.6: Rhythmic preset composition (temporal oscillations between reflection states)
Phase 2.7: Attractor visualization prompt generation (parameter → visual keywords)

Cost optimization: ~70% savings vs pure LLM approach.
"""

from fastmcp import FastMCP
from typing import Dict, List, Optional, Any, Tuple
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


# =============================================================================
# PHASE 2.6: RHYTHMIC PRESET COMPOSITION
# =============================================================================
# Normalized 5D parameter space for reflective surface morphospace.
# Each parameter maps the full taxonomy range to [0.0, 1.0].

REFLECTION_PARAMETER_NAMES = [
    "reflection_clarity",     # 0.0 = diffuse/scattered → 1.0 = perfect specular mirror
    "surface_roughness",      # 0.0 = mirror-smooth → 1.0 = heavily frosted/matte
    "metallic_character",     # 0.0 = dielectric (glass/water) → 1.0 = full metal (chrome/gold)
    "geometric_distortion",   # 0.0 = flat planar → 1.0 = compound curves/faceted
    "environmental_drama"     # 0.0 = overcast/soft → 1.0 = night urban/high contrast
]

REFLECTION_CANONICAL_STATES = {
    "mirror_still": {
        "reflection_clarity": 0.95,
        "surface_roughness": 0.02,
        "metallic_character": 0.05,
        "geometric_distortion": 0.00,
        "environmental_drama": 0.50,
        "_material_ref": "mirror_glass",
        "_geometry_ref": "flat",
        "_description": "Perfect planar mirror, undistorted specular reflection, full clarity"
    },
    "chrome_curve": {
        "reflection_clarity": 0.85,
        "surface_roughness": 0.05,
        "metallic_character": 0.95,
        "geometric_distortion": 0.55,
        "environmental_drama": 0.45,
        "_material_ref": "polished_chrome",
        "_geometry_ref": "convex",
        "_description": "Polished chrome convex surface, metallic sheen with fisheye compression"
    },
    "wet_street": {
        "reflection_clarity": 0.50,
        "surface_roughness": 0.30,
        "metallic_character": 0.00,
        "geometric_distortion": 0.05,
        "environmental_drama": 0.95,
        "_material_ref": "wet_pavement",
        "_geometry_ref": "flat",
        "_description": "Rain-slicked urban pavement, neon reflections in dark puddles, high drama"
    },
    "rippled_pool": {
        "reflection_clarity": 0.35,
        "surface_roughness": 0.40,
        "metallic_character": 0.00,
        "geometric_distortion": 0.45,
        "environmental_drama": 0.55,
        "_material_ref": "rippled_water",
        "_geometry_ref": "compound",
        "_description": "Moving water surface, dancing caustic patterns, warm ambient refraction"
    },
    "frosted_pane": {
        "reflection_clarity": 0.10,
        "surface_roughness": 0.85,
        "metallic_character": 0.00,
        "geometric_distortion": 0.05,
        "environmental_drama": 0.15,
        "_material_ref": "frosted_glass",
        "_geometry_ref": "flat",
        "_description": "Heavy frosted glass, diffuse scattered glow, soft overcast light"
    },
    "copper_facet": {
        "reflection_clarity": 0.70,
        "surface_roughness": 0.12,
        "metallic_character": 0.90,
        "geometric_distortion": 0.65,
        "environmental_drama": 0.55,
        "_material_ref": "copper",
        "_geometry_ref": "faceted",
        "_description": "Faceted copper surface, warm orange-tinted fragmented reflections"
    },
    "marble_hall": {
        "reflection_clarity": 0.65,
        "surface_roughness": 0.18,
        "metallic_character": 0.05,
        "geometric_distortion": 0.00,
        "environmental_drama": 0.40,
        "_material_ref": "polished_marble",
        "_geometry_ref": "flat",
        "_description": "Polished marble floor, luxury architectural reflection with veined pattern"
    },
    "gold_dome": {
        "reflection_clarity": 0.80,
        "surface_roughness": 0.08,
        "metallic_character": 1.00,
        "geometric_distortion": 0.50,
        "environmental_drama": 0.65,
        "_material_ref": "gold",
        "_geometry_ref": "convex",
        "_description": "Gold convex dome, warm yellow-tinted compressed panoramic reflection"
    }
}


REFLECTION_RHYTHMIC_PRESETS = {
    "clarity_sweep": {
        "state_a": "mirror_still",
        "state_b": "frosted_pane",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 16,
        "description": "Reflection clarity cycling from perfect specular mirror to heavy diffuse frost"
    },
    "urban_drama": {
        "state_a": "wet_street",
        "state_b": "chrome_curve",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 24,
        "description": "Alternating between rain-slicked urban puddles and industrial chrome curves"
    },
    "material_shift": {
        "state_a": "copper_facet",
        "state_b": "mirror_still",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 20,
        "description": "Metallic character transition from warm faceted copper to pure dielectric mirror"
    },
    "distortion_wave": {
        "state_a": "rippled_pool",
        "state_b": "marble_hall",
        "pattern": "triangular",
        "num_cycles": 4,
        "steps_per_cycle": 15,
        "description": "Geometric distortion oscillating between moving water caustics and flat stone"
    },
    "warmth_cycle": {
        "state_a": "gold_dome",
        "state_b": "frosted_pane",
        "pattern": "sinusoidal",
        "num_cycles": 2,
        "steps_per_cycle": 26,
        "description": "Temperature cycling from warm golden metallic dome to cool diffuse frost"
    }
}


def _generate_reflection_oscillation(
    num_steps: int,
    num_cycles: float,
    pattern: str
) -> List[float]:
    """Generate oscillation alpha values [0, 1] for reflection rhythmic presets."""
    values = []
    for i in range(num_steps):
        t = 2.0 * math.pi * num_cycles * i / num_steps

        if pattern == "sinusoidal":
            alpha = 0.5 * (1.0 + math.sin(t))
        elif pattern == "triangular":
            t_norm = (t / (2.0 * math.pi)) % 1.0
            alpha = 2.0 * t_norm if t_norm < 0.5 else 2.0 * (1.0 - t_norm)
        elif pattern == "square":
            t_norm = (t / (2.0 * math.pi)) % 1.0
            alpha = 0.0 if t_norm < 0.5 else 1.0
        else:
            alpha = 0.5 * (1.0 + math.sin(t))

        values.append(alpha)
    return values


def _get_reflection_state_coords(state_id: str) -> Dict[str, float]:
    """Get normalized parameter coordinates for a canonical reflection state."""
    state = REFLECTION_CANONICAL_STATES[state_id]
    return {p: state[p] for p in REFLECTION_PARAMETER_NAMES}


def _interpolate_reflection_states(
    state_a: Dict[str, float],
    state_b: Dict[str, float],
    alpha: float
) -> Dict[str, float]:
    """Linear interpolation between two reflection states."""
    return {
        p: state_a[p] * (1.0 - alpha) + state_b[p] * alpha
        for p in REFLECTION_PARAMETER_NAMES
    }


@mcp.tool()
def list_reflection_rhythmic_presets() -> str:
    """
    List all available Phase 2.6 rhythmic presets for reflective surfaces.

    Returns preset names, periods, patterns, state transitions, and descriptions.

    Cost: 0 tokens (dictionary access)
    """
    presets = {}
    for name, cfg in REFLECTION_RHYTHMIC_PRESETS.items():
        presets[name] = {
            "state_a": cfg["state_a"],
            "state_b": cfg["state_b"],
            "pattern": cfg["pattern"],
            "num_cycles": cfg["num_cycles"],
            "steps_per_cycle": cfg["steps_per_cycle"],
            "total_steps": cfg["num_cycles"] * cfg["steps_per_cycle"],
            "description": cfg["description"]
        }
    return json.dumps({
        "domain": "reflective_surfaces",
        "phase": "2.6",
        "preset_count": len(presets),
        "presets": presets,
        "available_periods": sorted(set(
            cfg["steps_per_cycle"] for cfg in REFLECTION_RHYTHMIC_PRESETS.values()
        )),
        "canonical_states": list(REFLECTION_CANONICAL_STATES.keys()),
        "parameter_names": REFLECTION_PARAMETER_NAMES
    }, indent=2)


@mcp.tool()
def generate_rhythmic_reflection_sequence(
    state_a_id: str,
    state_b_id: str,
    oscillation_pattern: str = "sinusoidal",
    num_cycles: int = 3,
    steps_per_cycle: int = 20,
    phase_offset: float = 0.0
) -> str:
    """
    Generate rhythmic oscillation between two reflection states.

    Phase 2.6 temporal composition for reflective surfaces.
    Creates periodic transitions cycling between surface types.

    Args:
        state_a_id: Starting state (mirror_still, chrome_curve, wet_street, etc.)
        state_b_id: Alternating state
        oscillation_pattern: "sinusoidal" | "triangular" | "square"
        num_cycles: Number of complete A→B→A cycles
        steps_per_cycle: Samples per cycle (this becomes the period)
        phase_offset: Starting phase (0.0 = A, 0.5 = B)

    Returns:
        Sequence with states, pattern info, and phase points

    Cost: 0 tokens (pure arithmetic)
    """
    if state_a_id not in REFLECTION_CANONICAL_STATES:
        return json.dumps({
            "error": f"Unknown state: {state_a_id}",
            "available": list(REFLECTION_CANONICAL_STATES.keys())
        }, indent=2)
    if state_b_id not in REFLECTION_CANONICAL_STATES:
        return json.dumps({
            "error": f"Unknown state: {state_b_id}",
            "available": list(REFLECTION_CANONICAL_STATES.keys())
        }, indent=2)

    total_steps = num_cycles * steps_per_cycle
    alphas = _generate_reflection_oscillation(total_steps, num_cycles, oscillation_pattern)

    if phase_offset > 0:
        offset_steps = int(phase_offset * steps_per_cycle)
        alphas = alphas[offset_steps:] + alphas[:offset_steps]

    state_a = _get_reflection_state_coords(state_a_id)
    state_b = _get_reflection_state_coords(state_b_id)

    sequence = []
    for i, alpha in enumerate(alphas):
        state = _interpolate_reflection_states(state_a, state_b, alpha)
        state["_step"] = i
        state["_alpha"] = round(alpha, 4)
        state["_phase"] = round((i % steps_per_cycle) / steps_per_cycle, 4)
        sequence.append(state)

    return json.dumps({
        "domain": "reflective_surfaces",
        "state_a": state_a_id,
        "state_b": state_b_id,
        "oscillation_pattern": oscillation_pattern,
        "num_cycles": num_cycles,
        "steps_per_cycle": steps_per_cycle,
        "total_steps": total_steps,
        "phase_offset": phase_offset,
        "parameter_names": REFLECTION_PARAMETER_NAMES,
        "sequence": sequence
    }, indent=2)


@mcp.tool()
def apply_reflection_rhythmic_preset(preset_name: str) -> str:
    """
    Apply a curated reflection rhythmic pattern preset.

    Phase 2.6 convenience tool with pre-configured patterns.

    Available presets:
    - clarity_sweep: mirror_still ↔ frosted_pane (period 16, specular ↔ diffuse)
    - urban_drama: wet_street ↔ chrome_curve (period 24, puddle ↔ metal)
    - material_shift: copper_facet ↔ mirror_still (period 20, metal ↔ dielectric)
    - distortion_wave: rippled_pool ↔ marble_hall (period 15, caustic ↔ flat)
    - warmth_cycle: gold_dome ↔ frosted_pane (period 26, warm metal ↔ cool frost)

    Cost: 0 tokens
    """
    if preset_name not in REFLECTION_RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset: {preset_name}",
            "available": list(REFLECTION_RHYTHMIC_PRESETS.keys())
        }, indent=2)

    cfg = REFLECTION_RHYTHMIC_PRESETS[preset_name]
    return generate_rhythmic_reflection_sequence(
        state_a_id=cfg["state_a"],
        state_b_id=cfg["state_b"],
        oscillation_pattern=cfg["pattern"],
        num_cycles=cfg["num_cycles"],
        steps_per_cycle=cfg["steps_per_cycle"]
    )


@mcp.tool()
def get_reflection_canonical_states() -> str:
    """
    Get all canonical reflection states with normalized parameter coordinates.

    These are the reference points in reflection morphospace used by
    Phase 2.6 presets and Phase 2.7 visualization.

    Cost: 0 tokens (dictionary access)
    """
    states = {}
    for state_id, state_data in REFLECTION_CANONICAL_STATES.items():
        states[state_id] = {
            "coordinates": {p: state_data[p] for p in REFLECTION_PARAMETER_NAMES},
            "material_ref": state_data["_material_ref"],
            "geometry_ref": state_data["_geometry_ref"],
            "description": state_data["_description"]
        }
    return json.dumps({
        "domain": "reflective_surfaces",
        "parameter_names": REFLECTION_PARAMETER_NAMES,
        "state_count": len(states),
        "states": states
    }, indent=2)


# =============================================================================
# PHASE 2.7: ATTRACTOR VISUALIZATION PROMPT GENERATION
# =============================================================================
# Visual vocabulary types mapping parameter coordinates to image-generation
# keywords. Each type represents a distinct visual archetype in reflection
# morphospace, identified by nearest-neighbor matching.

REFLECTION_VISUAL_TYPES = {
    "perfect_mirror": {
        "coords": {
            "reflection_clarity": 0.95,
            "surface_roughness": 0.02,
            "metallic_character": 0.05,
            "geometric_distortion": 0.00,
            "environmental_drama": 0.50
        },
        "keywords": [
            "flawless mirror reflection with perfect clarity",
            "undistorted specular surface doubling the scene",
            "silvered glass with razor-sharp reflected image",
            "planar mirror preserving all angles and proportions",
            "infinite depth illusion in mirror plane",
            "crystalline reflection fidelity"
        ],
        "optical_properties": {
            "finish": "perfect_specular",
            "dominant_wavelength": "scene_faithful",
            "edge_quality": "razor_sharp",
            "luminosity": "high_reflected"
        },
        "color_associations": [
            "true-color reflected scene", "silver-neutral surface tone",
            "deep virtual space behind glass", "clean highlight edges"
        ]
    },
    "metallic_gleam": {
        "coords": {
            "reflection_clarity": 0.82,
            "surface_roughness": 0.07,
            "metallic_character": 0.95,
            "geometric_distortion": 0.50,
            "environmental_drama": 0.55
        },
        "keywords": [
            "polished metal surface with tinted reflections",
            "lustrous chrome or gold sheen with color cast",
            "curved metallic body reflecting compressed panorama",
            "industrial gleam with directional highlight streaks",
            "warm or cool metallic tint over reflected imagery",
            "high-fidelity metal reflection with material color"
        ],
        "optical_properties": {
            "finish": "metallic_specular",
            "dominant_wavelength": "material_tinted",
            "edge_quality": "sharp_with_color_shift",
            "luminosity": "high_tinted"
        },
        "color_associations": [
            "chrome silver-blue tint", "copper warm orange cast",
            "gold rich yellow overlay", "brushed metal directional grain"
        ]
    },
    "rain_noir": {
        "coords": {
            "reflection_clarity": 0.50,
            "surface_roughness": 0.30,
            "metallic_character": 0.00,
            "geometric_distortion": 0.05,
            "environmental_drama": 0.95
        },
        "keywords": [
            "rain-slicked pavement reflecting neon city lights",
            "wet street mirror with elongated colored streaks",
            "dark puddle pools capturing inverted urban glow",
            "high-contrast night reflections on glossy asphalt",
            "cinematic wet-ground reflection with dramatic atmosphere",
            "noir lighting doubled in rain-polished surfaces"
        ],
        "optical_properties": {
            "finish": "wet_glossy",
            "dominant_wavelength": "neon_multicolor",
            "edge_quality": "soft_elongated",
            "luminosity": "contrast_extremes"
        },
        "color_associations": [
            "neon pink and blue streaks", "deep black wet asphalt",
            "sodium yellow streetlight pools", "reflected signage colors"
        ]
    },
    "caustic_dance": {
        "coords": {
            "reflection_clarity": 0.35,
            "surface_roughness": 0.40,
            "metallic_character": 0.00,
            "geometric_distortion": 0.45,
            "environmental_drama": 0.55
        },
        "keywords": [
            "dancing caustic light patterns on moving water",
            "rippled surface fragmenting reflected scene",
            "shimmering refracted light network across pool floor",
            "liquid surface with constantly shifting mirror fragments",
            "warm water reflections breaking into luminous ribbons",
            "organic distortion patterns from wave interference"
        ],
        "optical_properties": {
            "finish": "animated_caustic",
            "dominant_wavelength": "scene_fragmented",
            "edge_quality": "undulating_soft",
            "luminosity": "dappled_variable"
        },
        "color_associations": [
            "turquoise water-filtered light", "shifting warm gold patches",
            "blue-green refracted caustic network", "white dancing highlights"
        ]
    },
    "frost_diffuse": {
        "coords": {
            "reflection_clarity": 0.10,
            "surface_roughness": 0.85,
            "metallic_character": 0.00,
            "geometric_distortion": 0.05,
            "environmental_drama": 0.15
        },
        "keywords": [
            "heavy frosted glass with complete diffusion",
            "matte translucent surface scattering all light",
            "soft luminous glow through textured privacy glass",
            "no distinct reflection only ambient scattered radiance",
            "ethereal backlit frost with gentle gradients",
            "ice-crystal surface texture dissolving all imagery"
        ],
        "optical_properties": {
            "finish": "full_diffuse",
            "dominant_wavelength": "scattered_white",
            "edge_quality": "fully_dissolved",
            "luminosity": "low_ambient_glow"
        },
        "color_associations": [
            "milky translucent white", "soft blue-gray scattered light",
            "pale frost gradient", "warm backlight halo through glass"
        ]
    },
    "faceted_prism": {
        "coords": {
            "reflection_clarity": 0.70,
            "surface_roughness": 0.12,
            "metallic_character": 0.75,
            "geometric_distortion": 0.65,
            "environmental_drama": 0.55
        },
        "keywords": [
            "faceted crystal surface with fragmented reflections",
            "geometric prismatic separation of reflected scene",
            "cut-glass or gemstone multi-angle mirror planes",
            "each facet capturing a different perspective",
            "sharp-edged geometric reflection kaleidoscope",
            "architectural glass reflecting in discrete angular panels"
        ],
        "optical_properties": {
            "finish": "faceted_specular",
            "dominant_wavelength": "prismatic_split",
            "edge_quality": "sharp_geometric_borders",
            "luminosity": "high_variable_per_facet"
        },
        "color_associations": [
            "rainbow prismatic edge glints", "clear facet reflection panels",
            "warm copper or silver tinted planes", "sharp white highlight vertices"
        ]
    }
}


def _reflection_param_distance(
    state: Dict[str, float],
    target: Dict[str, float]
) -> float:
    """Euclidean distance between two states in reflection parameter space."""
    total = 0.0
    for p in REFLECTION_PARAMETER_NAMES:
        diff = state.get(p, 0.5) - target.get(p, 0.5)
        total += diff * diff
    return math.sqrt(total)


def _find_nearest_reflection_visual_type(
    state: Dict[str, float]
) -> Tuple[str, float, Dict[str, Any]]:
    """Find the nearest visual type to a given parameter state."""
    best_name = None
    best_dist = float("inf")
    best_data = None

    for type_name, type_data in REFLECTION_VISUAL_TYPES.items():
        dist = _reflection_param_distance(state, type_data["coords"])
        if dist < best_dist:
            best_dist = dist
            best_name = type_name
            best_data = type_data

    return best_name, best_dist, best_data


@mcp.tool()
def extract_reflection_visual_vocabulary(
    state: str
) -> str:
    """
    Extract visual vocabulary from reflection parameter coordinates.

    Phase 2.7 tool: Maps a 5D parameter state to the nearest canonical
    reflection visual type and returns image-generation-ready keywords.

    Uses nearest-neighbor matching against 6 visual types derived from
    the reflective surfaces taxonomy.

    Args:
        state: JSON dict with parameter coordinates:
            reflection_clarity, surface_roughness, metallic_character,
            geometric_distortion, environmental_drama

    Returns:
        Dict with nearest_type, distance, keywords,
        optical_properties, color_associations

    Cost: 0 tokens (pure Layer 2 computation)
    """
    try:
        state_dict = json.loads(state) if isinstance(state, str) else state
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON for state parameter"}, indent=2)

    nearest_name, distance, nearest_data = _find_nearest_reflection_visual_type(state_dict)

    return json.dumps({
        "nearest_type": nearest_name,
        "distance": round(distance, 4),
        "keywords": nearest_data["keywords"],
        "optical_properties": nearest_data["optical_properties"],
        "color_associations": nearest_data["color_associations"],
        "parameter_names": REFLECTION_PARAMETER_NAMES,
        "input_state": {p: state_dict.get(p, 0.5) for p in REFLECTION_PARAMETER_NAMES}
    }, indent=2)


@mcp.tool()
def generate_reflection_attractor_prompt(
    attractor_state: Optional[str] = None,
    preset_name: Optional[str] = None,
    mode: str = "composite",
    style_modifier: str = "",
    keyframe_count: int = 4
) -> str:
    """
    Generate image prompt from reflection attractor state or rhythmic preset.

    Phase 2.7 tool: Translates mathematical parameter coordinates into
    visual prompts suitable for image generation (ComfyUI, Stable Diffusion,
    DALL-E, etc.).

    Modes:
        composite: Single blended prompt from attractor state
        sequence: Multiple keyframe prompts from rhythmic preset trajectory

    Args:
        attractor_state: JSON parameter coordinates dict (for composite mode).
            If None, uses preset_name to generate from a preset midpoint.
        preset_name: Rhythmic preset name (for sequence mode, or as
            source for composite if attractor_state is None).
        mode: "composite" | "sequence"
        style_modifier: Optional prefix ("photorealistic", "cinematic", etc.)
        keyframe_count: Number of keyframes for sequence mode (default: 4)

    Returns:
        Dict with prompt(s), vocabulary details, and source metadata

    Cost: 0 tokens (Layer 2 deterministic)
    """
    if mode == "composite":
        if attractor_state is not None:
            try:
                state_dict = json.loads(attractor_state) if isinstance(attractor_state, str) else attractor_state
            except json.JSONDecodeError:
                return json.dumps({"error": "Invalid JSON for attractor_state"}, indent=2)
        elif preset_name and preset_name in REFLECTION_RHYTHMIC_PRESETS:
            cfg = REFLECTION_RHYTHMIC_PRESETS[preset_name]
            sa = _get_reflection_state_coords(cfg["state_a"])
            sb = _get_reflection_state_coords(cfg["state_b"])
            state_dict = _interpolate_reflection_states(sa, sb, 0.5)
        else:
            state_dict = _get_reflection_state_coords("mirror_still")

        nearest_name, distance, nearest_data = _find_nearest_reflection_visual_type(state_dict)

        keywords = nearest_data["keywords"]
        colors = nearest_data["color_associations"]

        prompt_parts = []
        if style_modifier:
            prompt_parts.append(style_modifier)
        prompt_parts.extend(keywords)
        prompt_parts.extend(colors[:2])

        return json.dumps({
            "mode": "composite",
            "prompt": ", ".join(prompt_parts),
            "vocabulary": {
                "nearest_type": nearest_name,
                "distance": round(distance, 4),
                "keywords": keywords,
                "optical_properties": nearest_data["optical_properties"],
                "color_associations": colors
            },
            "source": {
                "preset_name": preset_name,
                "state": {p: round(state_dict.get(p, 0.5), 4)
                          for p in REFLECTION_PARAMETER_NAMES}
            }
        }, indent=2)

    elif mode == "sequence":
        if not preset_name or preset_name not in REFLECTION_RHYTHMIC_PRESETS:
            return json.dumps({
                "error": "sequence mode requires a valid preset_name",
                "available": list(REFLECTION_RHYTHMIC_PRESETS.keys())
            }, indent=2)

        cfg = REFLECTION_RHYTHMIC_PRESETS[preset_name]
        total_steps = cfg["num_cycles"] * cfg["steps_per_cycle"]
        alphas = _generate_reflection_oscillation(
            total_steps, cfg["num_cycles"], cfg["pattern"]
        )
        sa = _get_reflection_state_coords(cfg["state_a"])
        sb = _get_reflection_state_coords(cfg["state_b"])

        step_indices = [
            int(i * (total_steps - 1) / (keyframe_count - 1))
            for i in range(keyframe_count)
        ]

        keyframes = []
        for idx in step_indices:
            alpha = alphas[idx]
            state = _interpolate_reflection_states(sa, sb, alpha)
            nearest_name, distance, nearest_data = _find_nearest_reflection_visual_type(state)

            kw = nearest_data["keywords"]
            colors = nearest_data["color_associations"]

            prompt_parts = []
            if style_modifier:
                prompt_parts.append(style_modifier)
            prompt_parts.extend(kw)
            prompt_parts.extend(colors[:2])

            keyframes.append({
                "step": idx,
                "alpha": round(alpha, 4),
                "prompt": ", ".join(prompt_parts),
                "nearest_type": nearest_name,
                "distance": round(distance, 4),
                "state": {p: round(state.get(p, 0.5), 4)
                          for p in REFLECTION_PARAMETER_NAMES}
            })

        return json.dumps({
            "mode": "sequence",
            "preset": preset_name,
            "description": cfg["description"],
            "keyframe_count": keyframe_count,
            "total_steps": total_steps,
            "period": cfg["steps_per_cycle"],
            "keyframes": keyframes
        }, indent=2)

    else:
        return json.dumps({
            "error": f"Unknown mode: {mode}",
            "available": ["composite", "sequence"]
        }, indent=2)


@mcp.tool()
def list_reflection_visual_types() -> str:
    """
    List all reflection visual vocabulary types for Phase 2.7 prompt generation.

    Returns the 6 canonical visual archetypes with their parameter coordinates,
    keywords, optical properties, and color associations.

    Cost: 0 tokens (dictionary access)
    """
    types = {}
    for type_name, type_data in REFLECTION_VISUAL_TYPES.items():
        types[type_name] = {
            "coords": type_data["coords"],
            "keyword_count": len(type_data["keywords"]),
            "keywords_preview": type_data["keywords"][:3],
            "optical_finish": type_data["optical_properties"]["finish"],
            "dominant_color": type_data["optical_properties"]["dominant_wavelength"]
        }
    return json.dumps({
        "domain": "reflective_surfaces",
        "phase": "2.7",
        "visual_type_count": len(types),
        "types": types,
        "usage": "Use extract_reflection_visual_vocabulary(state) to map coordinates to keywords"
    }, indent=2)


# =============================================================================
# UPDATED DOMAIN INFORMATION (Phase 2.6 + 2.7)
# =============================================================================

@mcp.tool()
def get_server_info() -> str:
    """
    Get information about the Reflective Surfaces MCP server.

    Returns server metadata, capabilities, and architecture overview.
    """
    return json.dumps({
        "server": "Reflective Surfaces MCP",
        "version": "2.0.0",
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
        "phase_2_6_enhancements": {
            "rhythmic_composition": True,
            "preset_count": len(REFLECTION_RHYTHMIC_PRESETS),
            "available_presets": list(REFLECTION_RHYTHMIC_PRESETS.keys()),
            "available_periods": sorted(set(
                cfg["steps_per_cycle"]
                for cfg in REFLECTION_RHYTHMIC_PRESETS.values()
            )),
            "canonical_state_count": len(REFLECTION_CANONICAL_STATES),
            "canonical_states": list(REFLECTION_CANONICAL_STATES.keys()),
            "parameter_names": REFLECTION_PARAMETER_NAMES
        },
        "phase_2_7_enhancements": {
            "attractor_visualization": True,
            "visual_type_count": len(REFLECTION_VISUAL_TYPES),
            "visual_types": list(REFLECTION_VISUAL_TYPES.keys()),
            "prompt_modes": ["composite", "sequence"],
            "supported_generators": [
                "ComfyUI", "Stable Diffusion", "DALL-E", "Midjourney"
            ]
        },
        "domain_registry_integration": {
            "domain_id": "reflective_surfaces",
            "parameter_names": REFLECTION_PARAMETER_NAMES,
            "preset_periods": sorted(set(
                cfg["steps_per_cycle"]
                for cfg in REFLECTION_RHYTHMIC_PRESETS.values()
            )),
            "period_interactions": {
                "shared_with_microscopy": [16, 20, 24],
                "shared_with_nuclear": [15],
                "shared_with_catastrophe": [15, 20],
                "shared_with_diatom": [15, 20],
                "shared_with_heraldic": [16],
                "shared_with_spark": [20],
                "unique_to_reflective": [26]
            }
        },
        "key_capabilities": [
            "Fresnel equation calculations",
            "Material optical property lookup",
            "Multi-factor reflection analysis",
            "Keyword detection and extraction",
            "Comparative scenario analysis",
            "Image prompt enhancement",
            "Phase 2.6 rhythmic preset composition",
            "Phase 2.7 attractor visualization prompts"
        ],
        "usage_pattern": "Call Layer 2 tools for deterministic analysis, then use results in Layer 3 for creative synthesis",
        "author": "Dal Marsters / Lushy Systems"
    }, indent=2)

if __name__ == "__main__":
    mcp.run()

"""
Optimization package for SeedVR2
Contains memory management, performance optimizations, and compatibility layers
"""
'''
# Memory management functions
from .memory_manager import (
    get_basic_vram_info,
    get_vram_usage,
    clear_memory, 
    reset_vram_peak,
)

# Performance optimization functions
from .performance import (
    optimized_video_rearrange,
    optimized_single_video_rearrange,
    optimized_sample_to_image_format,
    temporal_latent_blending,
)

# Compatibility functions and classes
from .compatibility import (
    FP8CompatibleDiT,
)

__all__ = [
    # Memory management
    "get_vram_usage",
    "clear_memory",
    "reset_vram_peak",
    
    # Performance optimization
    "optimized_video_rearrange",
    "optimized_single_video_rearrange",
    "optimized_sample_to_image_format",
    "temporal_latent_blending",
    
    # Compatibility
    "FP8CompatibleDiT",
] 
'''
import torch

class SwDSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (
                    ["SwD 2B, 6 steps", "SwD 2B, 4 steps", "SwD 8B, 6 steps", "SwD 8B, 4 steps"],
                    {"default": "SwD 2B, 6 steps"},
                ),
            },
        }

    RETURN_TYPES = ("INT", "STRING", "SIGMAS")
    RETURN_NAMES = ("img_size", "upscales", "SIGMAS")

    FUNCTION = "get_swd"

    CATEGORY = "SwD"

    def get_swd(self, preset):
        presets = {
            "SwD 2B, 6 steps": (
                256,
                "1.5, 2.0, 2.5, 3.0, 4.0",
                [1.0000, 0.9454, 0.8959, 0.7904, 0.7371, 0.6022, 0.0000],
            ),
            "SwD 2B, 4 steps": (
                256,
                "2.0, 3.0, 4.0",
                [1.0000, 0.9454, 0.7904, 0.6022, 0.0000],
            ),
            "SwD 8B, 6 steps": (
                256,
                "1.5, 2.0, 2.5, 3.0, 4.0",
                [1.0000, 0.9454, 0.8959, 0.7904, 0.7371, 0.6022, 0.0000],
            ),
            "SwD 8B, 4 steps": (
                512,
                "1.25, 1.5, 2.0",
                [1.0000, 0.8959, 0.7371, 0.6022, 0.0000],
            ),
        }

        img_size, upscales, float_list = presets[preset]
        return (img_size, upscales, torch.tensor(float_list, dtype=torch.float32))

NODE_CLASS_MAPPINGS = {
    "SwDSelector": SwDSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SwDSelector": "SwD Preset Selector",
}

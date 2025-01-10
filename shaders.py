import raylib
import os
import pickle

shaders = {}
shaders_enabled = True
shader_cache_file = 'shaders/shader_cache.pkl'

def load_shader_with_error_check(vs_path, fs_path):
    if fs_path not in shaders:
        shader = raylib.LoadShader(vs_path, fs_path)
        if shader.id == 0:
            raise ValueError(f"Failed to load shader from {fs_path}")
        shaders[fs_path] = shader
        save_shader_cache()
    return shaders[fs_path]

def save_shader_cache():
    with open(shader_cache_file, 'wb') as cache_file:
        pickle.dump(list(shaders.keys()), cache_file)

def load_shader_cache():
    if os.path.exists(shader_cache_file):
        with open(shader_cache_file, 'rb') as cache_file:
            cached_shaders = pickle.load(cache_file)
            for fs_path in cached_shaders:
                if isinstance(fs_path, str):
                    fs_path = fs_path.encode('utf-8')
                shader = raylib.LoadShader(b"", fs_path)
                shaders[fs_path] = shader

def load_shaders():
    load_shader_cache()
    try:
        shaders["lava"] = load_shader_with_error_check(b"", b"shaders/lava.fs")
        shaders["background"] = load_shader_with_error_check(b"", b"shaders/background.fs")
        shaders["main_menu_background"] = load_shader_with_error_check(b"", b"shaders/main_menu_background.fs")
        shaders["lighting"] = load_shader_with_error_check(b"", b"shaders/lighting.fs")
    except Exception as e:
        raise e
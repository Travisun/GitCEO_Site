import os
import pkgutil
import subprocess

def create_hexo_posts_for_standard_library_modules():
    for module in pkgutil.iter_modules():
        if module.name.startswith('_'):  # skip private modules
            continue
        module_name = module.name
        post_title = f"Python：{module_name}库高级用法举例和应用详解"
        command = f"hexo new \"{post_title}\""
        subprocess.run(command, shell=True)

create_hexo_posts_for_standard_library_modules()
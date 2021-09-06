import os
from clearml import Task
task = Task.init(project_name='NewWworks', task_name='Say Hello')
os.system("docker export 0b82f70087a6 > our_image.tar")
print("blablalbalallasl")


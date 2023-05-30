from workspace import models
import random


def code_generator():
    random_number = random.randint(1000000000, 9999999999)
    result = f"workspace{random_number}"
    workspace = models.Workspace.objects.filter(code=result)

    if workspace.exists():
        code_generator()
    else:
        return result
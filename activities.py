# @@@SNIPSTART python-project-template-activities
from temporalio import activity

@activity.defn
async def get_bowl():
    print('Getting bowl')

@activity.defn
async def put_bowl_away():
   print('Putting bowl away')

@activity.defn
async def add_cereal():
   print('Adding cereal')

@activity.defn
async def put_cereal_back_in_box():
   print('Putting cereal back in box')

@activity.defn
async def add_milk():
    print('Adding milk')

# @@@SNIPEND

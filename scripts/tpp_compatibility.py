import numpy
import Integration.🔥
import subprocess

list = []

class Control():
    def get_array(self, input):
        return numpy.array(input.numbers) * input.magnitude
    
    async def add_to_list(self, input):
        list += input
        
    def run_shell_script(self, input):
        subprocess.run(["sh", input.filename + ".sh"]):

"""
Predict the peptide sequence of transcripts
"""


import subprocess
from pathlib import Path
import os
import sys

from latch import small_task, large_task, workflow
from latch.types import LatchFile, LatchDir


@small_task
def get_orfpep_task(fasta: LatchFile, output_dir: LatchDir) -> LatchFile:
	out_basename = str(output_dir.remote_path)
	
	fasta_basename = str(os.path.basename(fasta.local_path))
	

	
	# commands
	_orfpep_cmd = ["TransDecoder.LongOrfs","-t", fasta.local_path]
	_orfpep2_cmd = ["TransDecoder.Predict","-t", fasta.local_path]
	subprocess.run(_orfpep_cmd)
	subprocess.run(_orfpep2_cmd)
	
	
	return LatchFile(f"{fasta_basename}.transdecoder.pep", f"{out_basename}/{fasta_basename}.transdecoder.pep")

@workflow
def transdecoder(fasta: LatchFile, output_dir: LatchDir) -> LatchFile:
    """
    

    __metadata__:
        display_name: Predict the peptide sequence of transcripts
        author:
            name: Corey Howe
            email: 	
            github: https://github.com/coreyhowe
        repository: https://github.com/coreyhowe/latch_transdecoder
        license:
            id: MIT

    Args:

        fasta:
          fasta file of assembled transcripts

          __metadata__:
            display_name: Fasta File
            
        output_dir:
          The directory where results will go.
          
          __metadata__:
            display_name: Output Directory
    """
    

    return get_orfpep_task(fasta=fasta, output_dir=output_dir) #, input_dir=input_dir)

#local execution
#if __name__ == "__main__":
       #transdecoder(
       #fasta=LatchFile("test.fasta"), 
       #output_dir=LatchDir("/root")) #reads=LatchFile("/users/von/neumann/machine.txt")

    

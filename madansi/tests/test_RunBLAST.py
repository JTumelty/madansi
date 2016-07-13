import unittest
from madansi.RunBLAST import RunBLAST
import filecmp
import os

class TestRunBLAST(unittest.TestCase):
    
  # def test_initialise_object(self):
  #     rb = RunBLAST('ab', 'cd', 'ef', 'gh', 'ij')
  #     self.assertTrue(rb.inputreference)
  #     self.assertTrue(rb.outputreference)
  #     self.assertTrue(rb.outputdatabase)
  #     self.assertTrue(rb.finaloutput)
  #     self.assertTrue(rb.queryfile)
  #     self.clean_up()
  #
  # def test_switch_columns(self):
  #     rb = RunBLAST('madansi/tests/data/input_reference.fa', 'outputreference' , 'outputdatabase', 'madansi/tests/data/input_query.fa','output_file')
  #     rb.run_switch_columns()
  #     self.assertTrue(filecmp.cmp('outputreference','madansi/tests/data/expected_output_reference.fa'))
  #     self.clean_up()
  #   
  # def test_reference_database(self):
  #     rb = RunBLAST('madansi/tests/data/input_reference.fa', 'madansi/tests/data/expected_output_reference.fa' , 'outputdatabase', 'madansi/tests/data/input_query.fa','output_file')
  #     rb.make_reference_database()
  #     self.assertTrue(os.path.isfile('outputdatabase.nin'))
  #     self.assertTrue(os.path.isfile('outputdatabase.nhr'))
  #     self.assertTrue(os.path.isfile('outputdatabase.nsq'))
  #     self.assertTrue(filecmp.cmp('outputdatabase.nsq', 'madansi/tests/data/expected_output_database.fa.nsq')) 
  #     self.assertTrue(filecmp.cmp('outputdatabase.nhr', 'madansi/tests/data/expected_output_database.fa.nhr'))
  #     self.clean_up()
      
    def test_run_BLAST(self):
        rb = RunBLAST('madansi/tests/data/input_reference.fa', 'madansi/tests/data/expected_output_reference.fa', 'outputdatabase', 'madansi/tests/data/input_query.fa', 'output_comparison')
        rb.make_reference_database()
        rb.run_BLAST()
        self.assertTrue(filecmp.cmp('output_comparison', 'madansi/tests/data/expected_comparison'))
        self.clean_up()
        
    def clean_up(self):
        for filename in ['outputreference', 'outputdatabase.nin', 'outputdatabase.nhr', 'outputdatabase.nsq']:
            if os.path.exists(filename):
                os.remove(filename)
        
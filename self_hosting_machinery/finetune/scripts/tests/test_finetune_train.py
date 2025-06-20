import torch
import unittest

class TestFinetuneTrain(unittest.TestCase):
    def test_init_process_group(self):
        try:
            torch.distributed.init_process_group(backend='nccl')
            self.assertTrue(torch.distributed.is_initialized())
        except Exception as e:
            self.fail(f"init_process_group raised an exception: {e}")

    def test_training_without_process_group(self):
        try:
            # Simulate a scenario where the process group is not initialized
            rank = torch.distributed.get_rank()
            self.fail("Expected ValueError when accessing rank without initializing process group")
        except ValueError:
            pass  # Expected behavior

if __name__ == '__main__':
    unittest.main()
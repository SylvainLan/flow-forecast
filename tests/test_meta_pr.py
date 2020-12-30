import torch
import unittest
from flood_forecast.meta_models.basic_ae import AE


class MetaModels(unittest.TestCase):
    def setUp(self):

        self.AE = AE(10, 128)

    def test_ae_init(self):
        self.assertEqual(self.AE.encoder_hidden_layer.input_shape, 10)
        self.assertEqual(self.AE(torch.rand(2, 10)).shape, (2, 128))

    def test_ae_2(self):
        self.assertEqual(self.AE.decoder_output_layer.output_shape, 128)

if __name__ == '__main__':
    unittest.main()
import assessment
import unittest
import sys 



class BasicTest(unittest.TestCase):
    
    def test_cost_region(self):
        input_x = [1,1,2,0]
        input_x_list = [100,200,50,300]
        self.assertEqual(assessment.cost_region(input_x,input_x_list),400)
    def test_minimum_cost(self):
        i = 1
        units = 3200
        cost = 28200
        cost_dict = assessment.NY_cost
        self.assertEqual(assessment.minimum_cost(i,units,cost,cost_dict),False)
    def test_resource_allocator(self):
        output = {"Output":[{
                "region":"New York",
                "total_cost":"$10150",
                "machines":[
                ("8XLarge",7),
                ("XLarge",1),
                ("Large",1)
                ]
                },
                {
                "region":"India",
                "total_cost":"$9520",
                "machines":[
                ("8XLarge",7),
                ("Large",3),
                ]
                },
                {
                "region":"China",
                "total_cost":"$8570",
                "machines":[
                ("8XLarge",7),
                ("XLarge",1),
                ("Large",1)
                ]
                },
                ]
                }
        self.assertEqual(assessment.resource_allocator(1,1150),output)
            
if __name__ == "__main__":
    unittest.main()
                
        

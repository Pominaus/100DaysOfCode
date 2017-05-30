using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grade_Results
{
    class GradeStatistics
    {
        public GradeStatistics()
        {
            
        }

        float highestVal;
        float minVal;
        float classAverage;

        public void setVals(List<float> lst)
        {
         
            highestVal = lst.Max();
            minVal = lst.Min();
            classAverage = lst.Average();
        }

        public void showVals()
        {
            Console.WriteLine("Highest Grade: " + highestVal + "\n" +
                                "Lowest Grade: " + minVal + "\n" + 
                                "Class average: " + classAverage);
        }
    }
}

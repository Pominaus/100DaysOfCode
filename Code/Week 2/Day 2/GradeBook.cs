using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grade_Results
{
    class GradeBook
    {
        List<float> gradeList = new List<float>();
        GradeStatistics GradeSummary = new GradeStatistics();

        public void SetGrades(float grade)
        {
            gradeList.Add(grade);
        }

        public void updateStats()
        {
            GradeSummary.setVals(gradeList);
        }

        public void ShowGrades()
        {
            updateStats();
            Console.WriteLine("\nClass Grades:\n===================\n");
            gradeList.ForEach(Console.WriteLine);
            Console.WriteLine("===================");
            GradeSummary.showVals();
            Console.WriteLine("===================");

        }
    }
}

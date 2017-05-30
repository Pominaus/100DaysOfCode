using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grade_Results
{
    class Program
    {
        static void Main(string[] args)
        {
            GradeBook ReportCard = new GradeBook();
            ReportCard.SetGrades(92);
            ReportCard.SetGrades(88.9f);
            ReportCard.SetGrades(91.3f);
            ReportCard.SetGrades(27);
            ReportCard.ShowGrades();
        }
    }
}

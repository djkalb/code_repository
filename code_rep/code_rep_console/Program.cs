using System;
using ModelLibrary;
using ModelLibrary.Models;

namespace code_rep_console
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var ctx = new RepositoryContext())
            {
                var user = new User() {
                    UserName = "iamme",
                    
                    IpAddress = "123456789"
                };

                ctx.Users.Add(user);
                ctx.SaveChanges();
            }
            Console.WriteLine("umm hell?");
        }
    }
}

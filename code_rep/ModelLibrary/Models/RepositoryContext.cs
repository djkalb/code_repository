using System;
using System.Collections.Generic;
using System.Text;
using System.Data.Entity;

namespace ModelLibrary.Models
{
    public class RepositoryContext : DbContext
    {
        public RepositoryContext() : base("Code_Rep")
        {
            Database.SetInitializer(new MigrateDatabaseToLatestVersion<RepositoryContext, Migrations.Configuration>());
        }
        public DbSet<Algorithm> Algorithms { get; set; }
        public DbSet<User> Users { get; set; }
        //public DbSet<State> States { get; set; }
        //public DbSet<Search> Searches { get; set; }
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {

        }

    }
}

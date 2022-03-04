namespace ModelLibrary.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class Code_Repv1 : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Algorithms",
                c => new
                    {
                        Id = c.Int(nullable: false, identity: true),
                        Language = c.String(),
                        Input = c.String(),
                        Description = c.String(),
                        Output = c.String(),
                        CodeBody = c.String(),
                        UserId = c.Int(nullable: false),
                        Removed = c.DateTime(),
                        IsPublic = c.Boolean(),
                    })
                .PrimaryKey(t => t.Id);
            
            CreateTable(
                "dbo.Users",
                c => new
                    {
                        UserId = c.Int(nullable: false, identity: true),
                        UserName = c.String(),
                        IpAddress = c.String(),
                        Algorithm_Id = c.Int(),
                    })
                .PrimaryKey(t => t.UserId)
                .ForeignKey("dbo.Algorithms", t => t.Algorithm_Id)
                .Index(t => t.Algorithm_Id);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.Users", "Algorithm_Id", "dbo.Algorithms");
            DropIndex("dbo.Users", new[] { "Algorithm_Id" });
            DropTable("dbo.Users");
            DropTable("dbo.Algorithms");
        }
    }
}

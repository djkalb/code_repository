using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace ModelLibrary
{
    public partial class Algorithm
    {
        [Key]
        public int Id { get; set; }
        public string Language { get; set; }
        public string Input { get; set; }
        public string Description { get; set; }
        public string Output { get; set; }
        public string CodeBody { get; set; }
        
        public int UserId { get; set; }
        
        
        // these two props probably belong in search, but they need to be entered on insertion
        public DateTime? Removed { get; set; }
        public bool? IsPublic { get; set; }

        
        public ICollection<User> Users { get; set; }
        //public virtual State State { get; set; }



        //    id = Column(Integer, primary_key= True, autoincrement= True)
        //language = Column(String(25))
        //input = Column(String(144))
        //description = Column(String(250), nullable=False)
        //ouput = Column(String(144))
        //code_body = Column(UnicodeText, nullable= False)
        //ipAddress = Column(Integer)
        //removed = Column(Boolean)
        //public = Column(Boolean)
    }
}

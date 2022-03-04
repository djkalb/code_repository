using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace ModelLibrary
{
    public partial class User
    {
        [Key]
        public int UserId { get; set; }
        public string UserName { get; set; }
        
        public string IpAddress { get; set; }
        
        //public Algorithm Algorithm { get; set; }
        //public virtual State State { get; set; }
    }
}

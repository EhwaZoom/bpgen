using System;
using System.Threading.Tasks;
using foo.Domain.Entities;

namespace foo.Data.Repositories {
    public interface IUserRepository : INHibernateRepository<User, Guid> { }
}
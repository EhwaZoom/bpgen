using System;
using foo.Data.Database;
using foo.Domain.Entities;
using NHibernate;

namespace mes_backend.Data.Repositories {
    public class UserRepository : NHibernateRepository<User, Guid>, IUserRepository {
        public UserRepository(IUnitOfWork<ISession> uow) : base(uow) { }
    }
}
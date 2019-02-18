using FluentNHibernate.Mapping;
using foo.Domain.Entities;

namespace foo.Data.Mappings {
    public class UserMapping : ClassMap<User> {
        public UserMapping() {
            Table("users");
            Id(x => x.Id).GeneratedBy.GuidComb();
        }
    }
}
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class EntrepotBD {

    private Connection co;

    public EntrepotBD(ConnexionMySQL co){
        this.co = co.getConnexion();
    }

    public int maxReference() throws SQLException {
        Statement st =  this.co.createStatement();
        ResultSet rs = st.executeQuery("Select ifNull(max(reference), 0) as mx from ARTICLE");
        rs.next();
        int res = rs.getInt("mx");
        rs.close();
        return res;
    }


    public Article getArticle(int num) throws SQLException {
        String st = "select * from ARTICLE where reference = ?";
        PreparedStatement ps =  this.co.prepareStatement(st);
        ps.setInt(1, num);
        ResultSet rs = ps.executeQuery();
        rs.next();
        Article res = new Article(rs.getInt(1), rs.getString(2), rs.getFloat(3));
        rs.close();
        return res;
    }

    public Article plusGrandIdArticle() throws SQLException{
        return getArticle(maxReference());
    }

    public List<Article> listArticle() throws SQLException{
        List<Article> res = new ArrayList<>();
        Statement st =  this.co.createStatement();
        ResultSet rs = st.executeQuery("Select reference from ARTICLE");
        while (rs.next()){
            res.add(getArticle(rs.getInt(1)));
        }
        return res;
    }

    public void entrepotParDepartement() throws SQLException{
        int cpt = 0;
        String prev = "";
        Statement st = this.co.createStatement();
        ResultSet rs = st.executeQuery("select code, nom, departement from ENTREPOT order by departement");
        while (rs.next()){
            if (! rs.getString("departement").equals(prev)){
                if (! prev.equals("")){
                    System.out.println("il y a " + cpt + "entrepot dans ce departement");
                }
                System.err.println("les entrepots dans le departement : " + rs.getString("departement"));
                cpt = 0;
            }
            System.out.println("    "+rs.getString("code") + " " + rs.getString("nom"));
            cpt ++;
            prev = rs.getString("departement");

        }

        if (cpt != 0)
            System.out.println("- il y a " + cpt + "entrepot dans ce departement");
        rs.close();

    }


    public void lesEntrepotsPossedeArticle(int num) throws SQLException{
        String req = "select code, nom, quantite from ENTREPOT natural join STOCKER where reference = ?";
        PreparedStatement ps = co.prepareStatement(req);
        ps.setInt(1, num);
        ResultSet rs = ps.executeQuery();
        while(rs.next()){
            System.out.println(rs.getString("code") + " " + rs.getString("nom") + " qte : " + rs.getString("quantite"));
        }
        rs.close();
    }


    public void lesArticlesPossedeParEntrepot(int num) throws SQLException{
        String req = "select reference, libelle, qte from ARTICLE natural join STOCKER where code = ?";
        PreparedStatement ps = co.prepareStatement(req);
        ps.setInt(1, num);
        ResultSet rs = ps.executeQuery();
        while(rs.next()){
            System.out.println(rs.getString("reference") + " " + rs.getString("libelle") + " qte : " + rs.getString("quantite"));
        }
        rs.close();
    }

    public float valeurEntrepot(int code) throws SQLException{
        float res = 0;
        String req = "select sum(quantite * prix) from STOCKER natural join ARTICLE where code = ?";
        PreparedStatement ps = co.prepareStatement(req);
        ps.setInt(1, code);
        ResultSet rs = ps.executeQuery();
        if (rs.next()){
            res = rs.getInt(1);
        }
        rs.close();
        return res;

    }

    public boolean existArticle(int ref) throws SQLException{
        PreparedStatement ps = this.co.prepareStatement("select * from ARTICLE where reference = ?");
        ps.setInt(1, ref);
        ResultSet rs = ps.executeQuery();
        if (rs.next()){
            return true;
        } else {
            return false;
        }
    }


    public void addOrUpdateArticle(Article article) throws Exception{
    Article a = getArticle(article.getReference());
    if (a != null) {
        if (a.getLibelle().equals(article.getLibelle())){
            String req = "update ARTICLE set ? where reference = ?";
            PreparedStatement ps = co.prepareStatement(req);
            ps.setFloat(1, article.getPrix());
            ps.setInt(2, a.getReference());
            ps.executeUpdate(req);


        } else {
            throw new Exception("y a un problème frère");
        }

    } else {
        String req = "insert into ARTICLE values (?, ?, ?)";
        PreparedStatement ps = co.prepareStatement(req);
        ps.setFloat(1, article.getReference());
        ps.setString(2, article.getLibelle());
        ps.setFloat(3, article.getPrix());
        ps.executeUpdate(req);

    }
}
    
}
